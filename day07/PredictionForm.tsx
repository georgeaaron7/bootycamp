
import React, { useState } from "react";

// Types provided to use
type PredictionInput = {
  text: string;
  threshold: number;
  includeMetadata: boolean;
};

type PredictionResult = {
  ok: boolean;
  input?: PredictionInput;
  prediction?: {
    label: string;
    score: number;
    info?: {
      timestamp?: string;
      model?: string;
      note?: string;
    };
  };
};

const BACKEND_URL = "http://localhost:3001/api/predict";

export default function PredictionForm() {
  // -----------------------------
  // Controlled form state (DONE)
  // -----------------------------
  const [text, setText] = useState("");
  const [threshold, setThreshold] = useState(50);
  const [includeMetadata, setIncludeMetadata] = useState(false);

  // -----------------------------------------
  // TODO:  must implement these:
  // -----------------------------------------
  // const [loading, setLoading] = useState(false);
  // const [error, setError] = useState<string | null>(null);
  // const [result, setResult] = useState<PredictionResult | null>(null);

  // -----------------------------------------
  // TODO: Implement form submit handler
  // Steps:
  //   1. preventDefault()
  //   2. set loading = true
  //   3. clear prev error + result
  //   4. POST to BACKEND_URL with fetch()
  //   5. await JSON result
  //   6. setResult(data)
  //   7. handle errors properly
  // -----------------------------------------
  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();

    // TODO: IMPLEMENT ME
    // Structure:
    //
    // setLoading(true);
    // setError(null);
    // setResult(null);
    //
    // try {
    //   const resp = await fetch(...);
    //   const json = await resp.json();
    //   setResult(json);
    // } catch (err) {
    //   setError("Something went wrong");
    // } finally {
    //   setLoading(false);
    // }
  }

  return (
    <form onSubmit={onSubmit} style={{ maxWidth: 600, margin: "0 auto" }}>
      <h2>Prediction Form — Day 07</h2>

      {/* Text input */}
      <label style={{ display: "block", marginBottom: 12 }}>
        Text:
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter text"
          style={{ display: "block", width: "100%", padding: 8 }}
        />
      </label>

      {/* Threshold slider */}
      <label style={{ display: "block", marginBottom: 12 }}>
        Threshold: {threshold}
        <input
          type="range"
          min={0}
          max={100}
          value={threshold}
          onChange={(e) => setThreshold(Number(e.target.value))}
          style={{ width: "100%" }}
        />
      </label>

      {/* Include metadata checkbox */}
      <label style={{ display: "block", marginBottom: 12 }}>
        <input
          type="checkbox"
          checked={includeMetadata}
          onChange={(e) => setIncludeMetadata(e.target.checked)}
        />
        Include Metadata
      </label>

      {/* Submit button */}
      <button type="submit">
        Predict
      </button>

      <br /><br />

      {/* TODO: Show loading message */}
      {/* {loading && <div>Loading...</div>} */}

      {/* TODO: Show error message */}
      {/* {error && <div style={{ color: "red" }}>{error}</div>} */}

      {/* TODO: Show pretty JSON result */}
      {/* 
      {result && (
        <pre style={{
          background: "#fff",
          padding: 12,
          borderRadius: 6,
          whiteSpace: "pre-wrap"
        }}>
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
      */}
    </form>
  );
}
