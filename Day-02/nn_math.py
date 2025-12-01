import math
import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def ReLU(x):
    return np.maximum(x,0)

def convolve(img,kernel):
    op_height = img.shape[0] - kernel.shape[0] + 1
    op_width = img.shape[1] - kernel.shape[1] + 1                          
    output = np.zeros((op_height,op_width))
    for i in range(op_height):
        for j in range(op_width):
            region = img[i : i + kernel.shape[0], j : j + kernel.shape[1]]
            output[i, j] = np.sum(region * kernel)
    return output

a = np.array([-1,0,2])

print(sigmoid(a))
print(ReLU(a))

image = np.array([
        [10, 10, 10, 0, 0],
        [-1, 10, 5, 0, 0],
        [10, 11, 10, 0, 0],
        [-2, 3, 10, 0, 0],
        [32, 10, 45, 0, 0]
    ])
kernel = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

print(convolve(image,kernel))
print(np.__version__)