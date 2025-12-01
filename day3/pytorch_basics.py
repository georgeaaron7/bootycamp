import torch
import numpy as np
 
# =============================================================
# Part A — Basic Tensor Manipulation
# =============================================================

print("\n=== Part A: Basic Tensor Manipulation ===")
print()

# Tensor Creation
print("\n--- Tensor Creation ---")
print()
# Created tensor using List 
data1 = [[1,2,3],[4,5,6],[7,8,9]]
t_list = torch.tensor(data1)
print("Tensor made from List: ", t_list)
print("    Shape: ", t_list.shape)
print("    Dtype: ", t_list.dtype)
print("    Device: ", t_list.device)
print()

# Created tensor using Array
data2 = np.array([[10,11,12],[13,14,15],[16,17,18]])
t_array = torch.from_numpy(data2)
print("Tensor made from Numpy: ", t_array)
print("    Shape: ", t_array.shape)
print("    Dtype: ", t_array.dtype)
print("    Device: ", t_array.device)
print()

# Created tensor using Random
t_random = torch.randn(3,3)
print("Tensor made using Random Tensor function: ", t_random)
print("    Shape: ", t_random.shape)
print("    Dtype: ", t_random.dtype)
print("    Device: ", t_random.device)

# Tensor Operations
print("\n--- Tensor Operations ---")
print()

# Addition
t_add = torch.add(t_list, t_array)
print("Addition of Tensors: ", t_list, " + ", t_array, " = ", t_add)
print()

# Multiplication
t_multiply = torch.multiply(t_list, t_array)
print("Multiplication of Tensors: ", t_list, " + ", t_array, " = ", t_multiply)
print()

# Matrix Multiplication
tf_list = t_list.float()
tf_array = t_array.float()
tf_matrixMul = torch.matmul(tf_list, tf_array)
print(" Matrix Multiplication of Tensors: ", tf_list, " + ", tf_array, " = ", tf_matrixMul)
print()

# Reshaping
tensor = torch.tensor([[1,2],[3,4],[5,6]])
tensorReshape = torch.reshape(tensor, (2,3))
print("Tensor before Reshaping: ", tensor)
print("Tensor after Reshaping: ", tensorReshape)
print()

# Indexing and Slicing
t_random[:,2] = 5
print("t_random before any operation: ", t_random)
print("t_random after replacing last column by 5: ", t_random)
print()

# =============================================================
# Part B — Autograd: Define & Verify a Gradient
# =============================================================

print("\n=== Part B: Autograd - Gradient Verification ===")
print()
x = torch.tensor(5.0, requires_grad=True) # Tensor Leaf 'x' (Integer tensors can't trace back gradients, so we use floating point.)
w = torch.tensor(6.0, requires_grad=True) # Tensor Leaft 'w'

print(x)
print(w)
L = 2*(x*3) + 3(w*2)(x**2) + 4*w*x + 5*w + 6*x + 7 # Function

print(f"L(x={x.item()}, w={w.item()}) = 2*(x*3) + 3(w*2)(x**2) + 4*w*x + 5*w + 6*x + 7")
print()
print(f"L (x={x.item()}, w={w.item()}) = ", L)

L.backward() # Using Backward function to calculate gradients

print("dL/dx =", x.grad) # Gradient of L wrt x at the value of x
print("dL/dw =", w.grad) # Gradient of L wrt w at the value of wgit checkout main