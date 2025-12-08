# -------------------------------------------------------------
# Day 3 - PyTorch Fundamentals (Starter Template)
# Goal:
# Understand PyTorch basics, manipulate tensors, and use autograd
# to define L = f(x, w) and verify gradients.
# -------------------------------------------------------------

import torch
import numpy as np

# =============================================================
# Part A — Basic Tensor Manipulation
# =============================================================

print("\n=== Part A: Basic Tensor Manipulation ===")

# ---------------------------
# 1. Create Tensors
# ---------------------------

print("\n--- Tensor Creation ---")
# TODO:
# Create tensors using:
# - Python lists
# - NumPy arrays
# - Random tensors (torch.randn)

# For each tensor, print:
# - shape
# - dtype
# - device (CPU/GPU)

#----------Solution Script-----------

#Tensor from Python Lists
tensor_data1 = [[1,2,3],[4,5,6],[7,8,9]]
tensor1 = torch.tensor(tensor_data1)
print(tensor1)
print(tensor1.shape)
print(tensor1.dtype)
print(tensor1.device)

#Tensor from numpy array
tensor_data2 = np.array([[10,20,30],[1,2,3]])
tensor2 = torch.tensor(tensor_data2)
print(tensor2)
print(tensor2.shape)
print(tensor2.dtype)
print(tensor2.device)

#Tensor from torch.rand()
torch.manual_seed(42)
tensor3 = torch.rand(4,3)
print(tensor3)
print(tensor3.shape)
print(tensor3.dtype)
print(tensor3.device)


# ---------------------------
# 2. Perform Basic Tensor Operations
# ---------------------------

print("\n--- Tensor Operations ---")
# TODO:
# Implement and print results of:
# - Addition
# - Multiplication
# - Matrix multiplication (@ or torch.matmul)
# - Reshaping (view or reshape)
# - Indexing and slicing

#------Solution Script----------
torch.manual_seed(100)
tensor_1 = torch.randint(size=(4,4),low = 1, high = 50)
torch.manual_seed(50)
tensor_2 = torch.randint(size=(4,4),low = 1, high = 50)
print(tensor_1)
print(tensor_2)
#Addition and Multiplication (Element-wise)
print("Addition-\n",tensor_1+tensor_2)
print("Multiplication-\n",tensor_1*tensor_2)
#Matrix Multiplication
print("Matrix Multiplication-\n",tensor_1.matmul(tensor_2))
#Reshaping, Indexing, Slicing
print(tensor_1.reshape(2,8)); #Reshape
print(tensor_1[:2,2:]) #Indexing and slicing


# =============================================================
# Part B — Autograd: Define & Verify a Gradient
# =============================================================

print("\n=== Part B: Autograd - Gradient Verification ===")

# TODO:
# - Create tensors with requires_grad=True
# - Define a simple function: L = f(x, w)
#   (You can choose polynomial, dot-product, etc.)
# - Compute output L
# - Call backward(): L.backward()
# - Print gradients using .grad
# - Verify manually if the gradient is correct

#------------Solution Script---------
x = torch.tensor(5.0, requires_grad = True)
w = torch.tensor(2.3, requires_grad = True)

L = (x)**2 + w #Function
print(L)    
L.backward()  #Compute the Backward pass
print(x.grad)
print(w.grad)

#Manual verification
def derivative_x(x,w):
  return 2*x
def derivative_w(x,w):
  return 1

print(derivative_x(x,w), derivative_w(x,w))


# =============================================================
# Expected Output Summary
# =============================================================

print("\n=== Script Must Print ===")
print("1. All created tensors")
print("2. Results of tensor operations")
print("3. Computed gradients using autograd")
