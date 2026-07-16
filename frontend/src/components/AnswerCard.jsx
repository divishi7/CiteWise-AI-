import "./AnswerCard.css";
import { useState } from "react";

function AnswerCard({ answer }) {
  const [copied, setCopied] = useState(false);


  const handleCopy = () => {
    navigator.clipboard.writeText(answer);

    setCopied(true);

    setTimeout(() => {
      setCopied(false);
    }, 2000);
  };

  return (

    <div className="answer-card">

      <div className="answer-header">

        <h2>AI Answer</h2>

        <span className="confidence">
          🟢 96% Confidence
        </span>

      </div>

      <div className="answer-text">

        {answer.split("\n\n").map((paragraph, index) => (
          <p key={index}>{paragraph}</p>
        ))}

      </div>

      <div className="answer-footer">

        <span className="generation-time">
          ⚡ Generated in 2.1 sec
        </span>

        <button
          className="copy-btn"
          onClick={handleCopy}
        >
          {copied ? "✓ Copied" : "📋 Copy Answer"}
        </button>

      </div>

    </div>

  );

}

export default AnswerCard;