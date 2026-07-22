import "./ChatBox.css";
import { useState } from "react";

const API_URL = "http://127.0.0.1:8000";

function ChatBox({
  setAnswer,
  setSources,
  setCrossAnalysis,
}) {
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (question.trim() === "") return;

    setLoading(true);

    try {
      const response = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to fetch response from backend");
      }

      const data = await response.json();

      console.log("Backend Response:", data);

      setAnswer(data.answer || "");
      setSources(data.sources || []);
      setCrossAnalysis(data.cross_analysis || "");

    } catch (error) {
      console.error("Chat Error:", error);
      alert("Failed to generate answer.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-box">
      <h2>Ask Questions</h2>

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
          {question.length}/500 characters
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