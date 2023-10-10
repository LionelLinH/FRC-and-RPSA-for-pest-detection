#!/usr/bin/env python
import logging
import os
import sys
import time
import torch
from torch.nn.parallel import DataParallel, DistributedDataParallel
from detectron2.config import LazyConfig, instantiate
from detectron2.engine import (
    SimpleTrainer,
    default_argument_parser,
    default_setup,
    hooks,
    launch,
)
from detectron2.engine.defaults import create_ddp_model
from detectron2.evaluation import inference_on_dataset, print_csv_format
from detectron2.utils import comm
from detectron2.utils.file_io import PathManager
from detectron2.utils.events import (
    CommonMetricPrinter,
    JSONWriter,
    TensorboardXWriter
)
from detectron2.checkpoint import DetectionCheckpointer
from detrex.utils import WandbWriter
from detrex.modeling import ema

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

os.environ["CUDA_LAUNCH_BLOCKING"] = "1"


def do_test(cfg, model, eval_only=False):
    logger = logging.getLogger("detectron2")

    if eval_only:
        logger.info("Run evaluation under eval-only mode")
        if cfg.train.model_ema.enabled and cfg.train.model_ema.use_ema_weights_for_eval_only:
            logger.info("Run evaluation with EMA.")
        else:
            logger.info("Run evaluation without EMA.")
        if "evaluator" in cfg.dataloader:
            ret = inference_on_dataset(
                model, instantiate(cfg.dataloader.test), instantiate(cfg.dataloader.evaluator)
            )
            print_csv_format(ret)
        return ret

    logger.info("Run evaluation without EMA.")
    if "evaluator" in cfg.dataloader:
        ret = inference_on_dataset(
            model, instantiate(cfg.dataloader.test), instantiate(cfg.dataloader.evaluator)
        )
        print_csv_format(ret)

        if cfg.train.model_ema.enabled:
            logger.info("Run evaluation with EMA.")
            with ema.apply_model_ema_and_restore(model):
                if "evaluator" in cfg.dataloader:
                    ema_ret = inference_on_dataset(
                        model, instantiate(cfg.dataloader.test), instantiate(cfg.dataloader.evaluator)
                    )
                    print_csv_format(ema_ret)
                    ret.update(ema_ret)
        return ret


def main(args):
    cfg = LazyConfig.load(args.config_file)
    cfg = LazyConfig.apply_overrides(cfg, args.opts)
    default_setup(cfg, args)
    model = instantiate(cfg.model)
    model.to(cfg.train.device)
    model = create_ddp_model(model)

    # using ema for evaluation
    ema.may_build_model_ema(cfg, model)
    DetectionCheckpointer(model, **ema.may_get_ema_checkpointer(cfg, model)).load(cfg.train.init_checkpoint)
    # Apply ema state for evaluation
    if cfg.train.model_ema.enabled and cfg.train.model_ema.use_ema_weights_for_eval_only:
        ema.apply_model_ema(model)
    print(do_test(cfg, model, eval_only=True))


if __name__ == "__main__":
    args = default_argument_parser().parse_args()
    launch(
        main,
        args.num_gpus,
        num_machines=args.num_machines,
        machine_rank=args.machine_rank,
        dist_url=args.dist_url,
        args=(args,),
    )