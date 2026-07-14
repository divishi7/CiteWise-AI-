import "./ChatBox.css";
import { useState } from "react";

function ChatBox() {
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = () => {
    if (question.trim() === "") return;

    setLoading(true);

    // Backend API yahan connect hogi
    setTimeout(() => {
      setLoading(false);
    }, 2000);
  };

  return (
    <div className="chat-box">

      <h2> Ask Questions</h2>

      <p className="chat-subtitle">
        Ask anything about your uploaded document.
      </p>

      <textarea
        placeholder="Ask anything about your uploaded PDF..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        maxLength={500}
        rows={6}
      />

      <div className="chat-footer">

        <span className="char-count">
          {question.length}/ 500 characters
        </span>

        <button
          className="ask-btn"
          onClick={handleSubmit}
          disabled={loading || question.trim() === ""}
        >
          {loading ? "Generating..." : "Generate Answer"}
        </button>

      </div>

    </div>
  );
}

export default ChatBox;