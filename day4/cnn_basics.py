# -------------------------------------------------------------
# Day 4 - PyTorch Neural Networks (Starter Template)
# Goal:
# Understand nn.Module lifecycle, build a CNN using nn.Conv2d
# and nn.MaxPool2d, and train it on a dummy dataset.
# -------------------------------------------------------------

import torch
import torch.nn as nn
import torch.optim as optim

# =============================================================
# Part A — nn.Module Lifecycle
# =============================================================

print("\n=== Part A: nn.Module Lifecycle ===")

# ---------------------------
# 1. Define a Simple Model
# ---------------------------

# TODO: Define a class that inherits from nn.Module

class neuralnetwork(nn.Module):
    
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10,20)
        self.fc2 = nn.Linear(20,1)

    def forward(self,x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

# ---------------------------
# 2. Instantiate and Inspect the Model
# ---------------------------

# TODO: Instantiate the model and print architecture

model = neuralnetwork()
print(model)

total_params = sum([n.numel() for n in model.parameters()])
print("Number of parameters : " , total_params)

# ---------------------------
# 3. Train and Evaluate Lifecycle
# ---------------------------

# TODO: Train the model on a dummy dataset

loss_fn = nn.MSELoss()

optimiser = optim.Adam(model.parameters() , lr = 0.01)

x = torch.randn(100 , 10)
y = torch.randint(0,2,(100,1) , dtype = torch.float)

uinput = input("enter the number of epochs : ")

num_epochs = int(uinput)

model.train()

for epoch in range(num_epochs):
    optimiser.zero_grad()
    predictions = model(x)
    loss = loss_fn(predictions , y)
    loss.backward()
    optimiser.step()
    print("Train loss:", loss.item())

x_test = torch.randn(20,10)
y_test = torch.randint(0,2,(20,1) , dtype = torch.float)

model.eval()
with torch.no_grad():
    output = model(x_test)
    e_loss = loss_fn(output , y_test)
    print("Test_loss:" , e_loss.item())

# =============================================================
# Part B — Build a Simple CNN
# =============================================================

print("\n=== Part B: Build a Simple CNN ===")

# TODO: Define a CNN class with nn.Conv2d and nn.MaxPool2d

class My_CNN(nn.Module):

    def __init__(self):
        super().__init__()
        
        self.conv1 = nn.Conv2d(3 , 6 ,3)
        self.pool1 = nn.MaxPool2d(2,2)
        self.conv2 = nn.Conv2d(6 , 12 , 3)
        self.fc = nn.Linear(12*1*1 , 2)

    def forward(self , x):
        x = torch.relu(self.conv1(x))
        x = self.pool(x)
        x = torch.relu(self.conv2(x))
        x = self.pool(x)
        x = x.view(x.size(0) , -1)
        x = self.fc(x)

        return x 

model = My_CNN()
print(model)

total_parameters = sum(p.numel() for p in model.parameters())
print("Number of Parameters : " , total_parameters)

# TODO: Train the CNN on a dummy dataset

x_train = torch.randn(100 , 3 , 10 , 10)
y_train = torch.randint(0,2, (100,))

x_test = torch.randn(20 , 3 , 10 , 10)
y_test = torch.randint(0,2,(20,))

loss_func = nn.CrossEntropyLoss()

optimiser = optim.Adam(model.parameters() , lr = 0.01)

model.train()

for n in range(num_epochs):
    optimiser.zero_grad()
    pred = model(x_train)
    loss = loss_func(pred , y_train)
    loss.backward()
    optimiser.step()
    print(f"Epoch {epoch+1}/{num_epochs} - Train Loss: {loss.item():.4f}")

model.eval()

with torch.no_grad():
    outputs = model(x_test)
    loss_e = loss_func(outputs , y_test)
    accuracy = (predicted == y_test).sum().item() / y_test.size(0)
    print(f"Test Loss: {test_loss.item():.4f} - Test Accuracy: {accuracy*100:.2f}%")


# =============================================================
# Expected Output Summary
# =============================================================

print("\n=== Script Must Print ===")
print("1. Model architecture")
print("2. Number of parameters")
print("3. Training and evaluation results")