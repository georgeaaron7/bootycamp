import { Router, Request, Response } from "express";

const router = Router();

/**
 * GET /api/predict
 * Info endpoint to check the route quickly.
 */
router.get("/predict", (_req: Request, res: Response) => {
  res.json({ ok: true, message: "Prediction endpoint (GET) — use POST /api/predict to get mocked predictions" });
});

/**
 * POST /api/predict
 * Body: { text?: string, threshold?: number, includeMetadata?: boolean }
 * Returns a mocked prediction JSON.
 */
router.post("/predict", (req: Request, res: Response) => {
  const { text = "", threshold = 50, includeMetadata = false } = req.body ?? {};

  // Create a mock score biased by threshold (simple deterministic-ish approach)
  const base = Math.max(0, Math.min(100, Number(threshold) || 50));
  // Add a small pseudo-randomness while keeping results sensible
  const score = Math.round(base + (Math.sin((text.length || 1) + Date.now() / 1000) + 1) * (100 - base) * 0.2);

  const mockedResponse = {
    ok: true,
    input: { text, threshold: base, includeMetadata },
    prediction: {
      label: text.trim() ? (score >= 60 ? "positive" : "negative") : "empty",
      score,
      ...(includeMetadata
        ? { info: { timestamp: new Date().toISOString(), model: "mock-v1", note: "mocked response" } }
        : {})
    }
  };

  // Intentionally return 200 with mocked payload
  res.json(mockedResponse);
});

export default router;
