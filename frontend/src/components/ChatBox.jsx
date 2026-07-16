import "./ChatBox.css";
import { useState } from "react";
import AnswerCard from "./AnswerCard";

const API_URL = "http://127.0.0.1:8000";

function ChatBox() {
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);
  const [answer, setAnswer] = useState("");

  const handleSubmit = () => {
    if (question.trim() === "") return;

    setLoading(true);

    fetch(`${API_URL}/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        question: question,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        setAnswer(data.answer);
        setLoading(false);
      })
      .catch((error) => {
        console.error(error);
        setLoading(false);
      });
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

      {answer && <AnswerCard answer={answer} />}
    </div>
  );
}

export default ChatBox;