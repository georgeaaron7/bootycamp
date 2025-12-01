import math
import numpy as np

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return x if x > 0 else 0


def convolve(image, kernel):
    img_rows = image.shape[0]
    img_cols = image.shape[1]
    ker_k = kernel.shape[0]
    output_rows = (img_rows - ker_k + 1)
    output_cols = (img_cols - ker_k + 1)
    output_matrix = np.zeros((output_rows, output_cols))
    for i in range(output_rows * output_cols):
        sum = 0
        out_r = i // output_cols
        out_c = i % output_cols
        for j in range(ker_k):
            for k in range(ker_k):
                sum = sum + (kernel[j][k] * image[j + out_r][k + out_c])
        output_matrix[out_r][out_c] = sum

    return output_matrix


image1 = np.array([
    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
])

kernel1 = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1],
])


output = convolve(image1, kernel1)
print(output)
