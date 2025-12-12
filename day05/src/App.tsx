import React from "react";
import PredictionForm from "./components/PredictionForm";

export default function App() {
  return (
    <div style={{ padding: 24, fontFamily: "system-ui, sans-serif" }}>
      <h1>BootyCamp — Day 05</h1>
      <p>Implement the PredictionForm component as described in README.md.</p>

      <div style={{ marginTop: 24 }}>
        <PredictionForm />
      </div>
    </div>
  );
}
