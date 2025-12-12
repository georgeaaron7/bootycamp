# Day 12: Computer Vision Basics — Image Representation & Simple Image Processing

Today marks your entry into the world of Computer Vision (CV) - the foundation behind image classification, object detection, face recognition, and everything visual in AI.


You get to see the moment where an ordinary picture turns into something a computer can actually understand. When you load an image, convert it to grayscale, and apply a threshold, you’re not just running code - you’re showing the system how to notice patterns, focus on important regions, and ignore the rest. This is the first step where you stop treating images like photos and start treating them like data a machine can learn from.


Before going into deep CNNs later, you must first understand:

• How images are represented inside a computer (pixels, channels).

• How to load & manipulate images.

• Basic operations like grayscale conversion and thresholding.

These fundamentals are used in every CV algorithm - from OpenCV scripts to advanced neural networks.

---

## 🧪 Main Goal
Understand digital image representation and perform basic image preprocessing using OpenCV.

By the end of today, you will:

✔ Install OpenCV (cv2)

✔ Load an image

✔ Convert it to grayscale

✔ Apply a threshold

✔ Display the results

These are essential for all future computer vision tasks.

## 🧠 Task 1: Conceptual Understanding
Before writing any code, you must study the basics of how computers "see" images. Study the following resources completely:

**Blog — Digital Image Fundamentals**  
You can see the geeksforgeeks one - https://www.geeksforgeeks.org/electronics-engineering/fundamental-steps-in-digital-image-processing/ or any other

**OpenCV Official Docs — Image Loading & Display**  
https://docs.opencv.org/master/d4/da8/group__imgcodecs.html

**YouTube — Basics of Image Processing with Python (OpenCV)**  
https://www.youtube.com/watch?v=oXlwWbU8l2o

## 🐍 Task 2: Hands-On Implementation (Python)

Navigate to your Day12 folder:

```bash
cd Day12/
 ```
Inside this folder, create the following Python file:
```bash
cv_basics.py
```

---

Inside this script, you must complete two core tasks:

🔹 **Part A — Basic Tensor Manipulation**

To build foundational understanding, implement the following:

1. **Load an Image Using OpenCV**

Read an image using 
```bash
cv2.imread
```
Print:

• shape

• datatype

• number of channels

2. **Convert to Grayscale**

Use
```bash
cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
Print grayscale shape & visualize it.

---

3. **Display All Outputs**

Use
```bash
cv2.imshow()
cv2.waitKey(0)
cv2.destroyAllWindows()
```
Show:

• Original image

• Grayscale image

• Thresholded image

---

If needed, you can use this template and fill in the TODO sections to complete the exercises
## ✍️Template 
```bash
# -------------------------------------------------------------
# Day 12 - Computer Vision Basics (Starter Template)
# Goal:
# Learn image representation, grayscale conversion, thresholding,
# and perform basic image preprocessing with OpenCV.
# -------------------------------------------------------------

import cv2

print("\n=== Part A: Load Image ===")

# TODO:
# 1. Load an image using cv2.imread("path")
# 2. Print:
#    - image shape
#    - dtype
#    - number of channels (if color)
# 3. Display the image using cv2.imshow()


print("\n=== Part B: Convert to Grayscale ===")

# TODO:
# 1. Convert the image to grayscale using cv2.cvtColor
# 2. Print the grayscale shape
# 3. Display the grayscale image


print("\n=== Part C: Apply Threshold ===")

# TODO:
# 1. Apply cv2.threshold with a simple binary threshold
# 2. Display the threshold output image
# 3. Add comments explaining what thresholding does


print("\n=== Expected Output ===")
print("1. Original image displayed")
print("2. Grayscale image displayed")
print("3. Thresholded binary image displayed")

cv2.waitKey(0)
cv2.destroyAllWindows()

```

## 💾 Task 3: Submission Using Feature Branching

Follow the exact Git workflow used in Day 1 and Day 2

**1. Synchronization & Branch Creation**

Create Day12 folder(if not already there). if its already created then navigate into it using ```bashcd Day12/```
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
git checkout -b feat/Day12-<your-name>
```

**2. Complete Task & Commit**

After finishing ```bashcv_basics.py```:
```bash
git add .
git commit -m "feat(Day12): Implemented basic CV operations using OpenCV"
```
**3. Push Your Branch**
```bash
git push -u origin feat/Day12-<your-name>
```
**4. Open the Pull Request (PR)**

1.Go to your fork on GitHub

2.Click Compare & Pull Request

3.Ensure source/destination is correct:

• From: your branch

• To: main branch of original bootcamp repo

4.PR Title Format
```
bash[D12] <Your Name> - PyTorch Tensor & Autograd Implementation
```

5.PR Description Must Include

✔ Loaded image using OpenCV
✔ Converted to grayscale
✔ Applied threshold
✔ Displayed all outputs
✔ File located inside Day12/

6.Click Create Pull Request.
