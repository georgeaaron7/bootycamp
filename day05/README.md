# 📘 Day 05 — Modern Frontend Setup (React + TypeScript)

## 🎯 Core Goal

Set up a modern frontend environment using **React + TypeScript**, understand typed components, and build a simple `PredictionForm` that captures user inputs and displays a mock prediction.
This forms the foundation for backend–frontend integration on **Day 06** and **Day 07**.

---

## 🧠 Reading / Theory / Topics to Cover

### 1. **React Component Model**

* What components are
* How state works
* How user inputs update state
* Declarative UI model

### 2. **TypeScript Basics (for React)**

* `type` vs `interface`
* Typed state and props
* Why TypeScript reduces frontend errors

### 3. **Vite (Project Setup Tool)**

* Why Vite is used for modern React apps
* How Vite scaffolds templates
* Running and building Vite apps

---

## 🎥 Useful YouTube Resources

* **React Concepts in 12 Minutes**
  [https://youtu.be/wIyHSOugGGw](https://youtu.be/wIyHSOugGGw)

* **TypeScript Crash Course**
  [https://youtu.be/d56mG7DezGs](https://youtu.be/d56mG7DezGs)

* **Vite Setup (React + TS)**
  [https://youtu.be/KCrXgy8qtjM](https://youtu.be/KCrXgy8qtjM)

---

## 📝 Problem Statement

Build a simple UI using React + TypeScript:

Your form must accept:

* A **text input**
* A **threshold slider** (0–100)
* A **checkbox**
* On submit → display **mock prediction result**

This demonstrates:

* Controlled components
* Typed React state
* Form submission handling
* Basic fetch-like workflow (mocked for now)

---

## 🛠️ Task 1 — Project Setup (Vite + React + TS)

From repo root:

```bash
mkdir Day-05
cd Day-05
npm create vite@latest . -- --template react-ts
npm install
npm run dev
```

Your app will start at:
➡️ **[http://localhost:5173](http://localhost:5173)**

---

## 🛠️ Task 2 — Create the Typed `PredictionForm` Component

Create file:

```
Day-05/src/components/PredictionForm.tsx
```

Your component must include:

* Typed state (`useState<{...}>`)
* Text input
* Range slider
* Checkbox
* Submit handler using a mocked `fetch()`
* Display of loading + result

---

## 🛠️ Task 3 — Integrate Component Into App

Edit:

```
Day-05/src/App.tsx
```

Import and render the `PredictionForm` so it displays on the main page.

---

## 📂 Final Folder Structure

```
Day-05/
  README.md
  package.json
  tsconfig.json
  index.html
  vite.config.ts
  src/
    main.tsx
    App.tsx
    components/
      PredictionForm.tsx
```

---

## 💾 Submission Workflow (Feature Branching)

### 1. Sync + Create Branch

```bash
git checkout main
git pull upstream main
git checkout -b feat/day-05-yourname
```

### 2. Commit Your Work

```bash
git add Day-05
git commit -m "feat(day05): React + TypeScript PredictionForm component"
```

### 3. Push to Origin

```bash
git push -u origin feat/day-05-yourname
```

### 4. Create Pull Request

**Base:** `main`
**From:** your feature branch

#### **PR Title**

```
[D05] <Your Name> — React + TypeScript PredictionForm
```

#### **PR Description**

```
Added Day-05 React + TypeScript project.
Includes typed PredictionForm component, App integration, and mock submit flow.
Location: Day-05/
```
