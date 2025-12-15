# Required Libraries
import numpy as np

# Sigmoid Activation Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# ReLU (Rectified Linear Unit) Activation Function
def relu(x):
    return np.maximum(0, x)

# Random Image as an Array
image = np.array([
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5]
])

# Kernel as an Array for horizontal edge detection
kernel = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
])

# Convolution Function
def convolve(image, kernel):
    imgH = len(image)
    imgW = len(image[0])
    kernelH = len(kernel)
    kernelW = len(kernel[0])

    # Output array size
    outH = imgH - kernelH + 1
    outW = imgW - kernelW + 1
    output = np.zeros((outH, outW))

    # Perform convolution
    for i in range(outH):
        for j in range(outW):
            area = image[i:i+kernelH, j:j+kernelW]  # Area of the image
            output[i, j] = np.sum(area * kernel)    # Element wise multiplication and sum
    return output

# Testing phase
print("Sigmoid:", sigmoid(np.array([-3, -2, -1, 0, 1, 2, 3])))
print("ReLU:", relu(np.array([-3, -2, -1, 0, 1, 2, 3])))
print("Convolution Output:\n", convolve(image, kernel))
