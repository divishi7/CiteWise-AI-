import "./ConflictPanel.css";

function ConflictPanel({ analysis }) {
  return (
    <div className="conflict-panel">

      <h2>⚖️ Cross-Source Analysis</h2>

      <p className="conflict-subtitle">
        AI-generated comparison of information retrieved from multiple documents.
      </p>

      {!analysis ? (

        <div className="summary-box">
          <h3>🧠 AI Interpretation</h3>
          <p>
            Upload multiple PDFs and ask a question that retrieves
            information from more than one document to generate a
            cross-source analysis.
          </p>
        </div>

      ) : (

        <div className="summary-box">

          <h3>🧠 AI Interpretation</h3>

          <div
            style={{
              whiteSpace: "pre-wrap",
              lineHeight: "1.7",
            }}
          >
            {analysis}
          </div>

        </div>

      )}

    </div>
  );
}

export default ConflictPanel;