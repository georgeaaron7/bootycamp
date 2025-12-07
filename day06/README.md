# 📘 Day 06 — Backend Setup + API (Node.js + Express + TypeScript)

## 🎯 Core Goal

Set up a simple backend server using **Node.js**, **Express**, and **TypeScript**.

This backend exposes two API endpoints:

* **GET `/health`** → confirms server is running
* **POST `/api/predict`** → returns mocked JSON so the frontend can integrate before ML is ready

This prepares the Day-05 frontend to communicate with a real backend on Day-07.

---

## 🧠 Reading / Theory / Topics to Cover

### 1. **Node.js Event Loop**

* How Node handles asynchronous operations
* Why backend APIs use non-blocking I/O
* Flow: **Call Stack → Event Queue → Worker Threads → Callback Queue**

### 2. **Express.js Basics**

* Setting up a server
* Defining routes
* Understanding middleware
* GET vs POST
* Sending JSON responses

### 3. **TypeScript in the Backend**

* Why typing helps
* Using `Request` and `Response` types
* Organizing code into a `routes/` folder

---

## 📝 Problem Statement

Build a minimal backend service that your Day-05 frontend can call.

### **Requirements**

* Server runs on **[http://localhost:3001](http://localhost:3001)**
* **GET `/health`** → returns `{ ok: true, uptime: number }`
* **POST `/api/predict`** → returns mocked prediction JSON
* Entire backend is written using **TypeScript**

---

## 🛠️ Task 1 — Backend Setup

```sh
mkdir day6
cd day6
npm init -y

npm install express
npm install -D typescript ts-node-dev @types/node @types/express cors @types/cors

npx tsc --init
```

### Modify `tsconfig.json`

Set:

```
"rootDir": "./src",
"outDir": "./dist"
```

### Add scripts to `package.json`

```json
"scripts": {
  "dev": "ts-node-dev --respawn --transpile-only src/server.ts",
  "build": "tsc",
  "start": "node dist/server.js"
}
```

---

## 🛠️ Task 2 — Create API Endpoints

### **Files Needed**

```
day6/src/server.ts
day6/src/routes/predict.ts
```

---

### **GET `/health`**

**Response example:**

```json
{
  "ok": true,
  "uptime": 123.456
}
```

---

### **POST `/api/predict`**

**Accepts:**

```json
{
  "text": "hello",
  "threshold": 70,
  "includeMetadata": true
}
```

**Returns mock prediction:**

```json
{
  "ok": true,
  "prediction": {
    "label": "positive",
    "score": 92,
    "info": {
      "timestamp": "...",
      "model": "mock-v1"
    }
  }
}
```

---

## 🛠️ Task 3 — Run & Test the Server

### Start development server:

```sh
npm run dev
```

### Test in browser or curl:

* `http://localhost:3001/health`
* `http://localhost:3001/api/predict`

### POST example:

```sh
curl -X POST http://localhost:3001/api/predict \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"hello\",\"threshold\":70}"
```

---

## 📂 Final Folder Structure

```
day6/
  README.md
  package.json
  tsconfig.json
  src/
    server.ts
    routes/
      predict.ts
```

---

## 🔗 Connecting to Day-05 Frontend

Frontend uses:

```ts
fetch("/api/predict")
```

Backend exposes the same route.

CORS is enabled through:

```ts
app.use(cors());
```

→ Frontend can call backend immediately during development.

---

## 💾 Submission Workflow

```sh
git checkout -b feat/day-06-backend
git add day6
git commit -m "feat(day06): Node + Express + TS backend with mocked API"
git push -u origin feat/day-06-backend
```

---

## ⭐ After This Day You Have

✔ A working backend
✔ A mocked ML prediction API
✔ Clean TypeScript backend architecture
✔ Frontend ↔ backend integration ready
✔ Foundation for Day-07 ML inference


