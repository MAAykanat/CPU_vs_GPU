import numpy as np
import matplotlib.pyplot as plt

from timeit import default_timer as timer

# from __future__ import print_function, division, absolute_import
from numba import cuda

@cuda.jit(device=True)
def mandelbrot(real, imaginary, max_iter):
    c = complex(real, imaginary)
    z = 0.0j
    i = 0

    for i in range(max_iter):
        z= z*z + c
        if (z.real*z.real + z.imag*z.imag) >=4:
            return i
        
        return 255
    
@cuda.jit
def crate_fractal(min_x, max_x, min_y, max_y, image, iters):
    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    x,y = cuda.grid(2)
    if x <width and y<height:
        real = min_x + x*pixel_size_x
        imaginary = min_y + y*pixel_size_y
        color = mandelbrot(real,imaginary,iters)
        image[y,x] = color
    # return image

image = np.zeros((500*10,750*10), dtype = np.uint8)

pixels = 500*10*750*10
nthred = 16
nblocksy = ((500*10) // nthred) + 1
nblocksx = ((750*10) // nthred) + 1

 
print(image.shape)
s = timer()
crate_fractal[(nblocksx,nblocksy),(nthred,nthred)](-2.0, 1.0, -1.0, 1.0, image, 20)
e=timer()

print(e-s)

plt.imshow(image)
plt.show()