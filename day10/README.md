# day 10: basic database persistence

## focus: sqlite + node.js

today your backend learns how to **remember**.

until now, your app could send data from frontend → node backend → ml service, but everything was temporary.
now we give the system a *memory* by integrating a lightweight SQL database   **SQLite**   to log every prediction request + response.

think of it as giving your backend a tiny journal so it can keep track of what the user asked, and what the ML model replied.

## **your checklist:**

1. **sqlite database setup:**

   * create a file-based SQLite database (`app.db` or `logs.db`).
   * make a table (e.g., `predictions`) with columns like:

     * `id` (integer primary key)
     * `input` (text)
     * `prediction` (text)
     * `timestamp` (text or datetime)

2. **node.js integration:**
   using `sqlite3` (or better: `better-sqlite3`):

   * open the database connection when the server starts
   * ensure table creation happens once (`CREATE TABLE IF NOT EXISTS ...`)

3. **logging inside the orchestrator route:**
   in your existing `/predict` route (from day 9):

   * take the incoming input
   * get the prediction from FastAPI
   * store both into the database as a new row

4. **CRUD basics:**
   today you're mostly doing:

   * **C**reate → inserting prediction logs
   * **R**ead → optional endpoint to list logs
     (update/delete not required today, but learn the concept)

5. **dependencies:**
   add to your project:

   * `sqlite3`
   * keep everything inside your `package.json`

## **crash course:**

### **sql vs nosql:**

before touching the database, [watch](https://www.youtube.com/watch?v=ruz-vK8IesE) a simple explanation of *why SQL still matters*:

your use case today is tiny but structured → SQLite fits perfectly.

### **sqlite3 API basics:**

watch these: [sqlite basics](https://youtu.be/8Xyn8R9eKB8?si=S0QrBgimFQZRTuK5) and [node js + sqlite](https://www.youtube.com/watch?v=mnH_1YGR2PM)

learn these functions:

```js
db.run()    // insert/create/update/delete
db.get()    // fetch one row
db.all()    // fetch multiple rows
```

### **express + database integration:**

[read this blog](https://medium.com/@gauravupadhyay786.gu/building-a-simple-crud-api-in-node-js-and-express-using-sqlite-a596a43c9ab9) on using SQLite inside express apps.
it’s extremely lightweight and mirrors real-world backend patterns.

## **useful stuff:**

### **database initialization (db.js):**

```js
const sqlite3 = require("sqlite3").verbose();

const db = new sqlite3.Database("./logs.db", (err) => {
  if (err) console.error(err);
  else console.log("sqlite database ready.");
});

db.run(`
  CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    input TEXT,
    prediction TEXT,
    timestamp TEXT
  )
`);

module.exports = db;
```

### **logging inside /predict route:**

```js
app.post("/predict", async (req, res) => {
  try {
    const input = req.body;

    const prediction = await getPrediction(input); // from mlClient.js

    const timestamp = new Date().toISOString();

    db.run(
      "INSERT INTO predictions (input, prediction, timestamp) VALUES (?, ?, ?)",
      [JSON.stringify(input), JSON.stringify(prediction), timestamp]
    );

    res.json({ prediction });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to log transaction" });
  }
});
```

### **optional endpoint: view logs**

```js
app.get("/logs", (req, res) => {
  db.all("SELECT * FROM predictions ORDER BY id DESC", (err, rows) => {
    if (err) return res.status(500).json({ error: "db error" });
    res.json(rows);
  });
});
```

## **final submission file**

your PR must include:

* `db.js` (or similar) where the SQLite connection + table creation happens
* updates to your node backend:

  * `/predict` route now logs input + prediction
  * optional `/logs` GET route
* updated `package.json` including `"sqlite3"`

