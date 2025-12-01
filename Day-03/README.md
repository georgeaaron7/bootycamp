# Day 3: PyTorch Fundamentals — Tensors & Autograd

Day 3 marks your transition from manually implementing mathematical operations (as you did on Day 2) to using real deep learning tools. Today, you will learn the foundations of PyTorch: tensors, tensor operations, and Autograd, which form the basis for building and training neural networks.

---

## 🧪 Main Goal
The ultimate goal is to understand PyTorch basics and implement simple tensor and gradient operations. You will use autograd to define a function L = f(x, w) and verify the gradient, and also implement a basic tensor manipulation script.

## 🧠 Task 1: Conceptual Understanding

Before writing any code, you must understand the core PyTorch concepts. Study the following resources completely:

**PyTorch Official Docs — What is a Tensor?**  
https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html

**Jeremy Howard — PyTorch Autograd Explained**  
https://www.youtube.com/watch?v=MswxJw-8PvE

**Blog — PyTorch Tensors vs NumPy Arrays**  
https://www.analyticsvidhya.com/blog/2021/06/pytorch-tensors-and-numpy-arrays/

## 🐍 Task 2: Hands-On Implementation (Python)

You will now write a script to practice tensors and autograd.
Navigate to your Day-03 folder:

```bash
cd Day3/
 ```
Inside this folder, create the following Python file:
```bash
pytorch_basics.py
```

---

Inside this script, you must complete two core tasks:

🔹 **Part A — Basic Tensor Manipulation**

To build foundational understanding, implement the following:

1. **Create Tensors**

Create tensors using:

• Python lists

• NumPy arrays

• Random tensors (```bashtorch.randn```)

For each tensor, print:

• shape

• dtype

• device

2. **Perform Basic Tensor Operations**

Implement and print results of:

• Addition

• Multiplication

• Matrix multiplication (```bash@``` or ```bashtorch.matmul```)

• Reshaping (```bashview``` or ```bashreshape```)

• Indexing and slicing

These operations help you understand how PyTorch handles data.

---

🔹 **Part B — Autograd: Define & Verify a Gradient**

The main objective is to use PyTorch’s automatic differentiation engine.

You must:

• Create tensors with ```bashrequires_grad=True```

• Define a simple function of the form: ```bashL = f(x, w)```

(You are free to choose the function — polynomial or dot-product based)

• Compute the output ```bashL```

• Call: ```bashL.backward()```

• Print the gradients using ```bash.grad```

• Verify that the gradient matches what you expect mathematically
This demonstrates how PyTorch builds a computational graph and computes gradients automatically.

📤 **What Your Script Must Print**

Your script must display:
1. All tensors created
2. Results of tensor operations
3. The computed gradients
   
---

If needed, you can use this template and fill in the TODO sections to complete the exercises
## ✍️Template 
```bash
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


# =============================================================
# Expected Output Summary
# =============================================================

print("\n=== Script Must Print ===")
print("1. All created tensors")
print("2. Results of tensor operations")
print("3. Computed gradients using autograd")
```

## 💾 Task 3: Submission Using Feature Branching

Follow the exact Git workflow used in Day 1 and Day 2

**1. Synchronization & Branch Creation**

Create Day3 folder(if not already there). if its already created then navigate into it using ```bashcd Day3/```
1. Switch to ```bashmain```:

```bash
git checkout main
```


2. Pull latest instructions:
```bash
git pull upstream main
```

3. Create your Day3 branch:
```bash
git checkout -b feat/day3-<your-name>
```

**2. Complete Task & Commit**

After finishing ```bashpytorch_basics.py```:
```bash
git add .
git commit -m "feat(day03): Implemented PyTorch tensor operations and autograd basics"
```
**3. Push Your Branch**
```bash
git push -u origin feat/day-03-<your-name>
```
**4. Open the Pull Request (PR)**

1.Go to your fork on GitHub

2.Click Compare & Pull Request

3.Ensure source/destination is correct:

• From: your branch

• To: main branch of original bootcamp repo

4.PR Title Format
```
bash[D03] <Your Name> - PyTorch Tensor & Autograd Implementation
```

5.PR Description Must Include

• Created tensors from lists, NumPy, and random data

• Performed tensor math operations

• Used autograd to compute gradients

• File located inside Day3/

6.Click Create Pull Request.
