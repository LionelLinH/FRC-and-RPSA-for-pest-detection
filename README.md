# FRC-and-RPSA-for-pest-detection
Codes for ***A transformer-based model with feature compensation and local information enhancement for end-to-end pest detection*** 


## Update
- [2023/10] Release our test code for the model on the IP102 and FPD datasets.


### 🏊 Training
**1. Virtual Environment**
```
# create virtual environment
conda create -n cddfuse python=3.8.10
conda activate cddfuse
# select pytorch version yourself
# install cddfuse requirements
pip install -r requirements.txt
```

**2. Data Preparation**

Download the MSRS dataset from [this link](https://github.com/Linfeng-Tang/MSRS) and place it in the folder ``'./MSRS_train/'``.

**3. Pre-Processing**

Run 
```
python dataprocessing.py
``` 
and the processed training dataset is in ``'./data/MSRS_train_imgsize_128_stride_200.h5'``.

**4. CDDFuse Training**

Run 
```
python train.py
``` 
and the trained model is available in ``'./models/'``.

### 🏄 Testing

**1. Pretrained models**

Pretrained models are available in ``'./models/CDDFuse_IVF.pth'`` and ``'./models/CDDFuse_MIF.pth'``, which are responsible for the Infrared-Visible Fusion (IVF) and Medical Image Fusion (MIF) tasks, respectively. 

**2. Test datasets**

The test datasets used in the paper have been stored in ``'./test_img/RoadScene'``, ``'./test_img/TNO'`` for IVF, ``'./test_img/MRI_CT'``, ``'./test_img/MRI_PET'`` and ``'./test_img/MRI_SPECT'`` for MIF.

Unfortunately, since the size of **MSRS dataset** for IVF is 500+MB, we can not upload it for exhibition. It can be downloaded via [this link](https://github.com/Linfeng-Tang/MSRS). The other datasets contain all the test images.

**3. Results in Our Paper**

If you want to infer with our CDDFuse and obtain the fusion results in our paper, please run 
```
python test_IVF.py
``` 
for Infrared-Visible Fusion and 
```
python test_MIF.py
``` 
for Medical Image Fusion. 

The testing results will be printed in the terminal. 

The output for ``'test_IVF.py'`` is:

```
================================================================================
The test result of TNO :
                 EN      SD      SF      MI     SCD     VIF     Qabf    SSIM
CDDFuse         7.12    46.0    13.15   2.19    1.76    0.77    0.54    1.03
================================================================================

================================================================================
The test result of RoadScene :
                 EN      SD      SF      MI     SCD     VIF     Qabf    SSIM
CDDFuse         7.44    54.67   16.36   2.3     1.81    0.69    0.52    0.98
================================================================================
```
which can match the results in Table 1 in our original paper.

The output for ``'test_MIF.py'`` is:

```
================================================================================
The test result of MRI_CT :
                 EN      SD      SF      MI     SCD     VIF     Qabf    SSIM
CDDFuse_IVF     4.83    88.59   33.83   2.24    1.74    0.5     0.59    1.31
CDDFuse_MIF     4.88    79.17   38.14   2.61    1.41    0.61    0.68    1.34
================================================================================

================================================================================
The test result of MRI_PET :
                 EN      SD      SF      MI     SCD     VIF     Qabf    SSIM
CDDFuse_IVF     4.23    81.69   28.04   1.87    1.82    0.66    0.65    1.46
CDDFuse_MIF     4.22    70.74   29.57   2.03    1.69    0.71    0.71    1.49
================================================================================

================================================================================
The test result of MRI_SPECT :
                 EN      SD      SF      MI     SCD     VIF     Qabf    SSIM
CDDFuse_IVF     3.91    71.81   20.66   1.9     1.87    0.65    0.68    1.45
CDDFuse_MIF     3.9     58.31   20.87   2.49    1.35    0.97    0.78    1.48
================================================================================
```
which can match the results in Table 5 in our original paper.
