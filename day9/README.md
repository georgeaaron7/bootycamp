# day 9: backend orchestration: the router mission

## focus: node.js + microservices


yesterday you wrapped your PyTorch model into its own **FastAPI microservice**.
today your job is to teach the **node.js backend** to act as the orchestrator the traffic controller that receives requests from React, forwards them to the Python model, and returns predictions cleanly back to the frontend.

think of node.js as the **middleman**:
frontend → node backend → ml model service → backend → frontend.

## **your checklist:**

1. **node.js backend:**
   assuming you already have a backend skeleton, today you will expand it by:

   * adding an **orchestrator route** (e.g., `POST /predict`).
   * inside this route, take incoming JSON from React.
   * forward that data to the FastAPI model microservice using **axios**.
   * receive the prediction, clean it, and send it back to the frontend.

2. **axios:**
   your node backend must communicate with the ML service like this:

   ```js
   const response = await axios.post("http://localhost:8000/predict", payload)
   ```

   * ensure you handle errors (`try/catch`).
   * forward only the necessary prediction result to the client.

3. **microservice flow:**
   keep the FastAPI server running in a separate terminal 
   keep the node backend running on its own port
   remember. these two services talk over **HTTP**, not function imports.

4. **clean structure:**

   * have a dedicated **service file** (e.g., `mlClient.js`) for axios calls.
     keeps your code clean and modular.
   * keep environment variables (URLs, ports) inside `.env`.

5. **dependencies:**
   update your `package.json` / submit a `package-lock.json` containing:

   * `axios`
   * `dotenv`
   * `express` (already there)

## **crash course:**

### **axios 101 for node:**

watch this video.[Axios API Requests](https://www.youtube.com/watch?v=ZEKBDXGnD4s&t=126s) it's a 40 min video and it covers the following 
* topics:
  * `axios.post(url, data)`
  * `axios.get(url)`
  * error handling (`error.response`, `error.message`)

### **node orchestrator pattern:**

you’re not training or running the model inside node.
node merely *passes messages*. this mirrors most of the real-world microservice architectures.

### **stuff to read:**

* **microservices communication patterns:**
  explains what and why. [what](https://www.geeksforgeeks.org/system-design/microservices-communication-patterns/) [why](https://strapi.io/blog/api-vs-web-service-differences-explained)

## **useful stuff:**

### **axios wrapper file:**

create a reusable module for ML calls:

```js
// mlClient.js
const axios = require("axios");

async function getPrediction(data) {
  const res = await axios.post(process.env.ML_URL + "/predict", data);
  return res.data;
}

module.exports = { getPrediction };
```

### **backend orchestrator route:**

```js
app.post("/predict", async (req, res) => {
  try {
    const prediction = await getPrediction(req.body);
    res.json({ prediction });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to reach ML service" });
  }
});
```

### **flow recap:**

* react sends `{input: [...]}` → node route `/predict`
* node forwards this JSON → fastapi `/predict`
* fastapi returns `{prediction: ...}`
* node returns this to react
* everybody wins

## **final submission file**

your PR must include:

* updated **node.js backend** with:

  * an orchestrator route
  * axios integration
  * clean error handling
  * optional `mlClient.js` service file

your backend should now successfully pass data from React → ML model → React.
if FastAPI is running, the node service should route predictions seamlessly.
