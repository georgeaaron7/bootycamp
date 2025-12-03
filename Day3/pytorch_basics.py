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

# From Python list
t_list = torch.tensor([1.0, 2.0, 3.0])
print("\nTensor from Python list:", t_list)
print("shape:", t_list.shape, "| dtype:", t_list.dtype, "| device:", t_list.device)

# From NumPy array
np_arr = np.array([[1, 2, 3], [4, 5, 6]])
t_numpy = torch.tensor(np_arr)
print("\nTensor from NumPy array:\n", t_numpy)
print("shape:", t_numpy.shape, "| dtype:", t_numpy.dtype, "| device:", t_numpy.device)

# Random tensor
t_rand = torch.randn(2, 3)
print("\nRandom tensor:\n", t_rand)
print("shape:", t_rand.shape, "| dtype:", t_rand.dtype, "| device:", t_rand.device)


# ---------------------------
# 2. Perform Basic Tensor Operations
# ---------------------------

print("\n--- Tensor Operations ---")

a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

# Addition
print("\nAddition:", a + b)

# Element-wise Multiplication
print("Multiplication:", a * b)

# Matrix multiplication
m1 = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
m2 = torch.tensor([[5.0, 6.0], [7.0, 8.0]])
print("\nMatrix Multiplication:\n", m1 @ m2)

# Reshaping
reshaped = m1.reshape(4)
print("\nReshaped Tensor:", reshaped)

# Indexing and slicing
print("\nIndexing m1[0,1]:", m1[0,1])
print("Slicing m1[:,0]:", m1[:,0])


# =============================================================
# Part B   Autograd: Define & Verify a Gradient
# =============================================================

print("\n=== Part B: Autograd - Gradient Verification ===")

# Create tensors requiring gradients
x = torch.tensor(3.0, requires_grad=True)
w = torch.tensor(4.0, requires_grad=True)

# Define function: L = (w*x + 5)^2
L = (w * x + 5) ** 2
print("\nLoss L:", L.item())

# Compute gradients
L.backward()

# Print gradients
print("\nGradient dL/dx:", x.grad)
print("Gradient dL/dw:", w.grad)

# Manual gradient verification:
# L = (wx + 5)^2
# dL/dx = 2(wx + 5)*w
# dL/dw = 2(wx + 5)*x
u = w.item() * x.item() + 5
print("\nManual dL/dx:", 2 * u * w.item())
print("Manual dL/dw:", 2 * u * x.item())


# =============================================================
# Expected Output Summary
# =============================================================

print("\n=== Script Must Print ===")
print("1. All created tensors")
print("2. Results of tensor operations")
print("3. Computed gradients using autograd")
