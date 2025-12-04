

\# 📘 Day 07 — Full Stack Communication (React → Node → Response)



\## 🎯 Core Goal



Establish \*\*real full-stack communication\*\* between the Day-05 React frontend and the Day-06 Node backend.



By the end of Day-07, your application should:



✔ Send a POST request from the UI using \*\*fetch()\*\*

✔ Reach the backend `/api/predict` endpoint

✔ Receive the mocked JSON response

✔ Display it inside the UI



This proves that your \*\*frontend + backend + network layer\*\* are working together end-to-end.



---



\# 🧠 Reading + 🎥 Video Resources (Short \& Relevant)



\## \*\*1. CORS (Cross-Origin Resource Sharing)\*\*



Why browsers block cross-origin requests and how the backend allows them.



\*\*Key ideas:\*\*



\* Same-origin policy

\* Preflight requests

\* `Access-Control-Allow-Origin`

\* Why `app.use(cors())` is needed



\*\*🎬 Video:\*\* Fireship — \*“CORS in 100 Seconds”\*

🔗 \[https://youtu.be/4KHiSt0oLJ0](https://youtu.be/4KHiSt0oLJ0)

(Perfect short explanation for this topic.)



---



\## \*\*2. fetch() API + Async/Await\*\*



Learn how to structure a fetch POST request:



```ts

fetch("/api/predict", {

&nbsp; method: "POST",

&nbsp; headers: { "Content-Type": "application/json" },

&nbsp; body: JSON.stringify({...})

});

```



\*\*Concepts:\*\*



\* Request method

\* JSON body

\* Headers

\* `await response.json()`

\* Error handling with try/catch



\*\*🎬 Video:\*\* freeCodeCamp — \*Asynchronous JavaScript (Callbacks → Promises → Async/Await)\*

🔗 \[https://youtu.be/ZYb\_ZU8LNxs](https://youtu.be/ZYb\_ZU8LNxs)

(This teaches everything you need for the React `onSubmit()` handler.)



---



\## \*\*3. Async/Await in React\*\*



How React components handle async code:



\* `loading` state

\* `error` state

\* `result` state

\* `async function onSubmit(e)`



---



\# 📝 Problem Statement



Your task today is to \*\*connect the UI and backend\*\*:



\### ✔ Enable CORS on backend



\### ✔ Build a typed form (`PredictionForm.tsx`) that collects:



\* text

\* threshold (0–100 slider)

\* checkbox



\### ✔ On submit → send POST request to backend



\### ✔ Show loading, errors, and result



This completes the frontend → backend → response loop.



---



\# 🛠️ Task 1 — Enable CORS on Backend



In:



```

day6/src/server.ts

```



Add:



```ts

import cors from "cors";

app.use(cors());

```



Restart server:



```bash

cd day6

npm run dev

```



Test that CORS header appears:



```bash

curl http://localhost:3001/health

```



Expect:



```

Access-Control-Allow-Origin: \*

```



---



\# 🛠️ Task 2 — Update `PredictionForm.tsx` (Frontend Template)



Open:



```

Day-05/src/components/PredictionForm.tsx

```



Replace the placeholder with this \*\*student task template\*\* (not a solution):



```tsx

// TODO: Day-07 Student Task

// Implement a fully typed form that:

// - collects text, threshold, includeMetadata

// - sends POST request using fetch()

// - displays loading, error, and result



export default function PredictionForm() {

&nbsp; // TODO: create state variables (text, threshold, includeMetadata)

&nbsp; // TODO: loading, error, result states



&nbsp; // TODO: implement async onSubmit using fetch()

&nbsp; // HINTS:

&nbsp; // - preventDefault()

&nbsp; // - setLoading(true)

&nbsp; // - POST to "http://localhost:3001/api/predict"

&nbsp; // - headers: JSON content type

&nbsp; // - body: JSON.stringify({...})

&nbsp; // - await resp.json()

&nbsp; // - handle errors with try/catch



&nbsp; return (

&nbsp;   <form>

&nbsp;     {/\* TODO: render text input \*/}

&nbsp;     {/\* TODO: render threshold range \*/}

&nbsp;     {/\* TODO: render checkbox \*/}

&nbsp;     {/\* TODO: render submit button \*/}

&nbsp;     {/\* TODO: show loading/error/result \*/}

&nbsp;     <div>PredictionForm goes here (Day-07 Task)</div>

&nbsp;   </form>

&nbsp; );

}

```



All important logic is left for the student to implement.



---



\# 🛠️ Task 3 — Integrate Into App



Open:



```

Day-05/src/App.tsx

```



Ensure:



```tsx

import PredictionForm from "./components/PredictionForm";



export default function App() {

&nbsp; return (

&nbsp;   <div style={{ padding: 24 }}>

&nbsp;     <h1>Prediction Demo (Day-07)</h1>

&nbsp;     <PredictionForm />

&nbsp;   </div>

&nbsp; );

}

```



---



\# 🛠️ Task 4 — Test Full Stack Communication



\### 1. Run Backend



```bash

cd day6

npm run dev

```



\### 2. Run Frontend



```bash

cd Day-05

npm run dev

```



\### 3. Visit:



```

http://localhost:5173/

```



\### 4. Submit the form



Expect:



\* Request reaches backend

\* Backend returns JSON

\* UI displays the result



If errors occur:



\* Check \*\*browser console\*\*

\* Check \*\*Network tab\*\*

\* Check \*\*backend logs\*\*



---



\# 🌐 Optional: Using Vite Proxy Instead of CORS



In:



```

Day-05/vite.config.ts

```



Add:



```ts

server: {

&nbsp; proxy: {

&nbsp;   "/api": "http://localhost:3001"

&nbsp; }

}

```



Then call:



```ts

fetch("/api/predict")

```



---



\# 📂 Final Folder Structure (After Day-07)



```

day6/

&nbsp; src/

&nbsp;   server.ts

&nbsp;   routes/predict.ts



Day-05/

&nbsp; src/

&nbsp;   App.tsx

&nbsp;   components/

&nbsp;     PredictionForm.tsx

&nbsp; vite.config.ts

```



---



\# 💾 Submission Workflow



\### 1. Create Branch



```bash

git checkout -b feat/day07-fullstack-yourname

```



\### 2. Commit



```bash

git add Day-05 day6

git commit -m "feat(day07): enable CORS and add PredictionForm template for full-stack communication"

```



\### 3. Push



```bash

git push -u origin feat/day07-fullstack-yourname

```



\### 4. Pull Request



\*\*PR Title\*\*



```

\[D07] <Your Name> — Full Stack Communication (CORS + fetch template)

```



\*\*PR Description\*\*



```

Implemented Day-07 foundational tasks:

\- Enabled CORS on backend

\- Added typed PredictionForm template for fetch() implementation

\- Linked component into App

\- Verified backend health and communication pathway



The fetch logic remains TODO for the student as required.

```



---



\# ⭐ After This Day You Have



✔ CORS-enabled backend

✔ A typed frontend form ready for fetch()

✔ Complete frontend → backend → response flow

✔ A clean template for the student to finish the fetch implementation



