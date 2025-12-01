import torch
import numpy as np


# -------------------------------------------------------------
# Day 3 - PyTorch Fundamentals (Starter Template)
# Goal:
# Understand PyTorch basics, manipulate tensors, and use autograd
# to define L = f(x, w) and verify gradients.
# ------------------------------------------------------------- 

# =============================================================
# Part A — Basic Tensor Manipulation
# =============================================================

print("\n=== Part A: Basic Tensor Manipulation ===","\n")


# Create tensors using:

# 1.Python lists
array = [[1,2,3],[7,8,9],[10,11,2]]
t = torch.tensor(array)
print("Tensor from python list: ",t)
print("Shape : ",t.shape)
print("Datatype : ",t.dtype)
print("Device : ",t.device,"\n")

# 2.NumPy arrays
a = np.ones((2,2))
np_to_tensor = torch.from_numpy(a)
print("Tensor from python list: ",np_to_tensor)
print("Shape : ",np_to_tensor.shape)
print("Datatype : ",np_to_tensor.dtype)
print("Device : ",np_to_tensor.device,"\n")

# 3.Random tensors (torch.randn)
b = torch.randn(3,3)
print("Tensor from python list: ",b)
print("Shape : ",b.shape)
print("Datatype : ",b.dtype)
print("Device : ",b.device,"\n")

# ---------------------------
# 2. Perform Basic Tensor Operations
# ---------------------------

print("\n--- Tensor Operations ---")
 
arr1 = torch.tensor([[2.,3.],[12.,23.]])
arr2 = torch.tensor([[1.,9.],[6.,7.]])

# Implement and print results of:
# - 1.Addition
print("Addition: \n",arr1.add(arr2),"\n")

# - 2.Multiplication
print("Element wise multiplication: \n",arr1.mul(arr2),"\n")

# - 3.Matrix multiplication (@ or torch.matmul)
print("Matrix multiplication : \n",arr1.matmul(arr2),"\n")

# - 4.Reshaping (view or reshape)
arr1_reshaped = arr1.reshape(1, 4)
arr2_reshaped = arr2.reshape(1, 4)

print("arr1 reshaped:\n", arr1_reshaped)
print("arr2 reshaped:\n", arr2_reshaped,"\n")

# - 5.Indexing and slicing
print("Row 1 of arr1 : \n", arr1[1,:])
print("Last column of arr2 : \n",arr2[:,-1])

# =============================================================
# Part B — Autograd: Define & Verify a Gradient
# =============================================================

print("\n=== Part B: Autograd - Gradient Verification ===\n")




# TODO:
# - Create tensors with requires_grad=True
# - Define a simple function: L = f(x, w)
#   (You can choose polynomial, dot-product, etc.)
# - Compute output L
# - Call backward(): L.backward()
# - Print gradients using .grad
# - Verify manually if the gradient is correct



x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
w = torch.tensor([0.1, 0.2, 0.3], requires_grad=True)

print("Tensor x:", x)
print("Tensor w:", w)

L = (x @ w) ** 2
print("Function L :", L)

L.backward()  

print("\nGradient for x:", x.grad)
print("Gradient for w:", w.grad)

manual_gradx = 2 * (x @ w) * w
manual_gradw = 2 * (x @ w) * x

print("\nManual gradient for x:", manual_gradx)
print("Manual gradient for w:", manual_gradw)