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

Please do not hesitate to contact.

# How to Install CUDA
    Intallation of Cuda and using it on tensorflow has 5 steps: 
   * Uninstall old tensorflow and all its components (tensorflow-gpu, tensorflow-intel )
   * Check Compability between components ([Link](https://www.tensorflow.org/install/source_windows)):
        * Python Version
        * Tensorflow Version
        * CUDA SDK Version
        * CudaDNN Version*
   * If it is necessary, install different python version. Tensorflow-gpu does not support higher than python 3.10 up to now.
   * Install Nvidia Graphics Card & Drivers (you most probably already have)
   * Download and install CUDA SDK
   * Download CudaDNN zip file, and extract them on where cuda installed. most probably--> C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2

