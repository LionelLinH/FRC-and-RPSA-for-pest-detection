# FRC-and-RPSA-for-pest-detection
Codes for ***A transformer-based model with feature compensation and local information enhancement for end-to-end pest detection*** 


## Update
- [2023/10] Release our test code for the model on the IP102 and FPD datasets.


###  Testing
**1. Experimental Environment**
```
# create environment
conda create -n pest_detection python=3.7 -y
conda activate pest_detection
pip install -r requirements.txt
```

**2. Data Preparation**

Download the IP102 dataset from [this link](https://github.com/xpwu95/IP102) and place it in the folder ``'./IP102/'``.
Download the FPD dataset from [this link](https://www.frontiersin.org/articles/10.3389/fpls.2022.857104/full) and place it in the folder ``'./FPD/'``.

**3. Pretrained models**
Pretrained models are available in ``'./models/pest_detection_IP102.pth'`` and ``'./models/pest_detection_FPD.pth'``, which can be downloaded via [this link](https://pan.baidu.com/s/1UjzxSL94mPZlp-GMM1XMxg 
code：y7z7).
**4. Results in Our Paper**

If you want to infer with our model and obtain the results in our paper, please run 
```
python test.py
``` 
The testing results will be printed in the terminal. 

The output for IP102 is:

```
[06/13 06:36:35] d2.evaluation.coco_evaluation INFO: Evaluation results for bbox: 
|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 35.641 | 57.268 | 38.842 | 12.659 | 34.541 | 36.813 |
[06/13 06:36:35] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 
| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| 0          | 57.922 | 1          | 20.276 | 2          | 50.204 |
| 3          | 43.177 | 4          | 33.971 | 5          | 33.563 |
| 6          | 44.322 | 7          | 30.500 | 8          | 38.797 |
| 9          | 13.557 | 10         | 41.303 | 11         | 26.010 |
| 12         | 30.072 | 13         | 50.589 | 14         | 54.989 |
| 15         | 51.393 | 16         | 59.460 | 17         | 9.772  |
| 18         | 41.879 | 19         | 14.397 | 20         | 35.639 |
| 21         | 41.577 | 22         | 53.932 | 23         | 25.523 |
| 24         | 40.106 | 93         | 0.041  | 101        | 2.621  |
| 25         | 66.295 | 26         | 57.429 | 27         | 20.660 |
| 28         | 0.755  | 29         | 11.259 | 30         | 15.025 |
| 31         | 58.131 | 32         | 30.364 | 33         | 43.697 |
| 34         | 42.581 | 35         | 5.961  | 36         | 18.247 |
| 37         | 52.050 | 38         | 20.110 | 39         | 29.728 |
| 40         | 48.750 | 41         | 45.355 | 42         | 31.416 |
| 43         | 61.988 | 44         | 35.250 | 45         | 23.578 |
| 46         | 10.658 | 47         | 38.957 | 48         | 33.428 |
| 49         | 13.416 | 50         | 29.374 | 51         | 37.738 |
| 52         | 2.404  | 53         | 40.046 | 54         | 24.960 |
| 55         | 43.476 | 56         | 16.565 | 57         | 23.013 |
| 58         | 10.652 | 61         | 80.000 | 62         | 53.820 |
| 64         | 42.540 | 65         | 54.300 | 66         | 73.888 |
| 67         | 69.047 | 68         | 59.855 | 69         | 49.924 |
| 70         | 43.644 | 71         | 33.541 | 72         | 67.723 |
| 73         | 30.644 | 74         | 24.026 | 76         | 53.109 |
| 77         | 35.136 | 78         | 31.776 | 79         | 15.203 |
| 81         | 37.983 | 82         | 22.239 | 83         | 32.170 |
| 84         | 56.577 | 85         | 16.803 | 86         | 30.701 |
| 87         | 51.940 | 88         | 54.948 | 89         | 1.555  |
| 90         | 36.011 | 91         | 2.500  | 92         | 15.846 |
| 94         | 61.292 | 95         | 60.600 | 96         | 33.669 |
| 97         | 15.665 | 98         | 0.164  | 99         | 59.709 |
| 100        | 59.728 |            |        |            |        |
[06/13 06:36:38] d2.evaluation.testing INFO: copypaste: Task: bbox
[06/13 06:36:38] d2.evaluation.testing INFO: copypaste: AP,AP50,AP75,APs,APm,APl
[06/13 06:36:38] d2.evaluation.testing INFO: copypaste: 35.6412,57.2680,38.8422,12.6590,34.5411,36.8130
```
which can match the results in Table 3 in our original paper.

The output for FPD is:

```
|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 95.319 | 99.163 | 98.219 | 68.908 | 90.767 | 97.803 |
[06/22 02:12:54] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 
| category                            | AP      | category                                   | AP      | category                                 | AP      |
|:------------------------------------|:--------|:-------------------------------------------|:--------|:-----------------------------------------|:--------|
| Drosicha_contrahens_female          | 96.163  | Drosicha_contrahens_male                   | 100.000 | Chalcophora_japonica                     | 100.000 |
| Anoplophora_chinensis               | 98.210  | Psacothea_hilaris(Pascoe)                  | 98.434  | Apriona_germari(Hope)                    | 99.246  |
| Monochamus_alternatus               | 100.000 | Plagiodera_versicolora(Laicharting)        | 93.811  | Latoia_consocia_Walker                   | 100.000 |
| Hyphantria_cunea                    | 97.088  | Cnidocampa_flavescens(Walker）              | 99.180  | Cnidocampa_flavescens(Walker_pupa)       | 75.335  |
| Erthesina_fullo                     | 90.057  | Erthesina_fullo_nymph-2                    | 85.885  | Erthesina_fullo_nymph                    | 93.251  |
| Spilarctia_subcarnea(Walker）        | 90.499  | Psilogramma_menephron                      | 100.000 | Sericinus_montela                        | 99.550  |
| Sericinus_montela_larvae            | 93.882  | Clostera_anachoreta                        | 100.000 | Micromelalopha_troglodyta(Graeser)       | 98.676  |
| Latoia_consocia_Walker_larvae       | 95.976  | Plagiodera_versicolora(Laicharting)_larvae | 89.930  | Plagiodera_versicolora(Laicharting)_ovum | 87.450  |
| Spilarctia_subcarnea(Walker)_larvae | 97.454  | Spilarctia_subcarnea(Walker)_larvae-2      | 92.628  | Psilogramma_menephron_larvae             | 98.965  |
| Cerambycidae_larvae                 | 94.475  | Micromelalopha_troglodyta(Graeser)_larvae  | 90.956  | Hyphantria_cunea_larvae                  | 98.199  |
| Hyphantria_cunea_pupa               | 99.591  |                                            |         |                                          |         |
[06/22 02:12:54] d2.evaluation.testing INFO: copypaste: Task: bbox
[06/22 02:12:54] d2.evaluation.testing INFO: copypaste: AP,AP50,AP75,APs,APm,APl
[06/22 02:12:54] d2.evaluation.testing INFO: copypaste: 95.3191,99.1631,98.2187,68.9080,90.7667,97.8032
```
which can match the results in Table 4 in our original paper.
