
const express = require("express");
// require cors in a way that works whether it's default-exported or CommonJS
const _cors = require("cors");
const cors = _cors.default ?? _cors;

// keep types for Request/Response/NextFunction
import type { Request, Response, NextFunction } from "express";

// require the router and use .default if necessary
const predictRouter = require("./routes/predict").default ?? require("./routes/predict");

// create app & port
const app = express();
const PORT = process.env.PORT ? Number(process.env.PORT) : 3001;



// Middlewares
app.use(cors()); // simple dev CORS allow. Remove or restrict for production.
app.use(express.json());

// Basic health endpoint
app.get("/health", (_req: Request, res: Response) => {
  res.json({ ok: true, uptime: process.uptime() });
});

// Mount API router
app.use("/api", predictRouter);

// Simple global error handler
app.use((err: any, _req: Request, res: Response, _next: NextFunction) => {
  console.error("Unhandled error:", err);
  res.status(500).json({ ok: false, error: "Internal server error" });
});

app.listen(PORT, () => {
  console.log(`Server listening on http://localhost:${PORT}`);
});
