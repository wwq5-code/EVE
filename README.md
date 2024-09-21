# CAP

# CAP: Towards Verification of Machine Unlearning via Customized Adversarial Perturbation
## Overview
This repository is the official implementation of CAP, and the corresponding paper is under review.


## Prerequisites

```
python = 3.10.10
torch==2.0.0
torchvision==0.15.1
matplotlib==3.7.1
numpy==1.23.5
```

We also show the requirements packages in requirements.txt

Here, we demonstrate the overall evaluations, which are also the main achievement claimed in the paper. We will explain the results and demonstrate how to achieve these results using the script and corresponding parameters.

Evaluated on NVIDIA Quadro RTX 6000 GPUs,
### TABLE I: General Evaluation Results on MNIST, CIFAR10, STL-10, and CelebA:

On MNIST, ESR=2%

| On MNIST             | Original    | MIB      |   CAP   | 
| --------             | --------    | -------- | -------- |  
| Running time (s)     | 142         | 146      |  12.81     |  
| Unl. Verifiability   | -           | 100.0%   | 100.0%   |   
| Accuracy (Original)  | 98.91%      | 98.73%   | 98.91%  |  
| Accuracy (Unlearned) | -           | 97.51%   | 97.69%   |  
 
 

In this table, we can achieve these metric values by running corresponding python files.


1. To run the CAP on MNIST, we can run
```
python /CAP_for_unl_veri/CAP_experiment/On_MNIST/MNIST_CAP_R_Restart_RFU.py
```


2. To run the CAP on CIFAR10, we can run
```
python /CAP_for_unl_veri/CAP_experiment/On_CIFAR10/CIFAR10_CAP_RFU.py
```

3. To run the CAP on STL-10, we can run

```
python /CAP_for_unl_veri/CAP_experiment/On_STL10/STL10_CAP_RFU.py
```

4. To run the CAP on CelebA, we can run

```
python /CAP_for_unl_veri/CAP_experiment/On_CelebA/CelebA_CAP_RFU.py
```
Note that, to sucessfully run the program on CelebA, we need first prepare the CelebA dataset, which can be downloaded from: 
(https://drive.google.com/drive/folders/0B7EVK8r0v71pWEZsZE9oNnFzTm8?resourcekey=0-5BR16BdXnb8hVj6CNHKzLg)