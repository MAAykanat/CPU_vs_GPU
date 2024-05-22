# Tabla of Contents

   * [About Repo](#about-repo)
   * [How to Install CUDA](#how-to-install-cuda)
   * [Requirements](#requirements)
   * [Discussion](#discussion)
   * [Referance](#referance)
   * [Authors](#authors)

# About Repo
How to install and use CUDA properly. Then, how to use it by using tensorflow and numba.

Follow steps below [How to Install CUDA](#how-to-install-cuda)

It has been tested in Windows.

Please do not hesitate to contact.

# How to Install CUDA
    Intallation of Cuda and using it on tensorflow has 5 steps: 
   1. Uninstall old tensorflow and all its components (tensorflow-gpu, tensorflow-intel )
   2. Check Compability between components ([Link](https://www.tensorflow.org/install/source_windows)):
        * Python Version
        * Tensorflow Version
        * CUDA SDK Version
        * CudaDNN Version*
   3. If it is necessary, install different python version. Tensorflow-gpu does not support higher than python 3.10 up to now.
   4. Install Nvidia Graphics Card & Drivers (you most probably already have)
   5. Download and install CUDA SDK
   6. Download CudaDNN zip file, and extract them on where cuda installed. most probably --> C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2 


&darr; &darr; &darr; Inside the zip file &darr; &darr; &darr;
![Step-6](CudaDNN_inside_zip.png "CuDNN")

&darr; &darr; &darr; Where to extract &darr; &darr; &darr;
![Step-6](Cuda_directory.png "Cuda Directory")

   7. Verify by simple program on cmd. 

    python tf_check.py



