import numpy as np
# 1.sigmoid

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 2.relu
def relu(x):
    return x * (x > 0)

# 3.  `convolve(image, kernel)`:
#      Define a small 5x5 "image" (matrix).
#       Define a 3x3 "kernel" (e.g., a vertical edge detector).
#      Write the nested loops to slide the kernel over the image and calculate the output feature map.

def convolve(image, kernel):
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape
    output_height = image_height - kernel_height + 1
    output_width = image_width - kernel_width + 1

    output = np.zeros((output_height, output_width))

    for i in range(output_height):
        for j in range(output_width):
            region = image[i:i+kernel_height, j:j+kernel_width]
            output[i, j] = np.sum(region * kernel)
    return output

print(sigmoid(np.array([-2,-1, 0, 1, 2])))

print(relu(np.array([-1, 0, 1, 2])))

image = np.array([[3, 4, 3, 0, 7],
                  [3, 1, 2, 6, 0],
                  [1, -1, 1, 2, -3],
                  [-3, -1, 0, 1, 4],
                  [2, -2, 0, 0, 1]])
kernel = np.array([[1, 0, -1],
                   [1, 0, -1],
                   [1, 0, -1]])
print(convolve(image, kernel))

