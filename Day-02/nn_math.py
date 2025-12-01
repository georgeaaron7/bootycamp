import numpy as np 

def sigmoid(x):
    return 1/(1+np.exp(-x))

def ReLU(x):
    return np.maximum(0,x)

def convolve(image , kernl):

    kernl_verlnth , kernl_horlnth = kernl.shape
    image_verlnth , image_horlnth = image.shape

    output_verlnth = image_verlnth - kernl_verlnth + 1
    output_horlnth = image_horlnth - kernl_horlnth + 1

    output = np.zeros((output_verlnth, output_horlnth))

    for i in range(output_verlnth):
        for j in range(output_horlnth):
            sliced_img = image[i:i+kernl_verlnth , j:j+kernl_horlnth]
            output[i,j] = np.sum(sliced_img*kernl)

    return output

test = np.array([-2, 5, -7, 1, 3])


print("Sigmoid result : " , sigmoid(test))
print("ReLU result : " , ReLU(test))

image = np.array([
    [3, 1, 2, 4, 0],
    [0, 1, 3, 2, 5],
    [4, 2, 1, 0, 3],
    [5, 1, 0, 2, 4],
    [2, 3, 4, 1, 0]
]
)

kernl = np.array([[-2,0,2],[-2,0,2],[-2,0,2]])

print("output : " , convolve(image,kernl))