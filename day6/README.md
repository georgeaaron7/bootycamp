📘 Day 06 — Backend Setup + API (Node.js + Express + TypeScript)

🎯 Core Goal



Set up a simple backend server using Node.js, Express, and TypeScript.

This backend will expose:



GET /health → to confirm the server is running



POST /api/predict → returns mocked JSON (so frontend can integrate before ML service exists)



This prepares Day-05 frontend to talk to a real backend on Day-07.



🧠 Reading / Theory / Topics to Cover

1\. Node.js Event Loop



How Node handles asynchronous operations



Why backend APIs use non-blocking I/O



The flow: Call Stack → Event Queue → Worker Threads → Callback Queue



2\. Express.js Basics



Setting up a server



Defining routes



Understanding middleware



GET vs POST



Sending JSON



3\. TypeScript in Backend



Why typing helps



Using Request and Response



Organizing code into a routes/ folder



📝 Problem Statement



Build a minimal backend service that your Day-05 frontend can call.



Requirements:



Server runs on http://localhost:3001



GET /health → { ok: true, uptime: number }



POST /api/predict → returns mocked prediction JSON



Built using TypeScript



🛠️ Task 1 — Backend Setup

mkdir day6

cd day6

npm init -y

npm install express

npm install -D typescript ts-node-dev @types/node @types/express cors @types/cors

npx tsc --init





Modify tsconfig.json: set

rootDir → src

outDir → dist



Add to package.json:



"scripts": {

&nbsp; "dev": "ts-node-dev --respawn --transpile-only src/server.ts",

&nbsp; "build": "tsc",

&nbsp; "start": "node dist/server.js"

}



🛠️ Task 2 — Create API Endpoints



Files:



day6/src/server.ts

day6/src/routes/predict.ts



GET /health



Returns:



{ "ok": true, "uptime": 123.456 }



POST /api/predict



Accepts:



{

&nbsp; "text": "hello",

&nbsp; "threshold": 70,

&nbsp; "includeMetadata": true

}





Returns mock prediction:



{

&nbsp; "ok": true,

&nbsp; "prediction": {

&nbsp;   "label": "positive",

&nbsp;   "score": 92,

&nbsp;   "info": { "timestamp": "...", "model": "mock-v1" }

&nbsp; }

}



🛠️ Task 3 — Run \& Test



Start dev server:



npm run dev





Test:



http://localhost:3001/health



http://localhost:3001/api/predict



POST example:



curl -X POST http://localhost:3001/api/predict \\

&nbsp; -H "Content-Type: application/json" \\

&nbsp; -d "{\\"text\\":\\"hello\\",\\"threshold\\":70}"



📂 Final Folder Structure

day6/

&nbsp; README.md

&nbsp; package.json

&nbsp; tsconfig.json

&nbsp; src/

&nbsp;   server.ts

&nbsp;   routes/

&nbsp;     predict.ts



🔗 Connecting to Day-05 Frontend



Frontend uses:



fetch("/api/predict")





Backend exposes the same route.



Because we added:



app.use(cors());





→ Frontend connects immediately.



💾 Submission Workflow

git checkout -b feat/day-06-backend

git add day6

git commit -m "feat(day06): Node + Express + TS backend with mocked API"

git push -u origin feat/day-06-backend



⭐ After This Day You Have:



✔ A working backend

✔ A mock ML prediction API

✔ A clean TS backend architecture

✔ Integration with the Day-05 frontend

✔ A foundation for Day-07 real ML inference

