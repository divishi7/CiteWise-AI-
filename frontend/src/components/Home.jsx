import { useState } from "react";
import Navbar from "./Navbar";
import UploadCard from "./UploadCard";
import ChatBox from "./ChatBox";
import CitationPanel from "./CitationPanel";
import ConflictPanel from "./ConflictPanel";
import AnswerCard from "./AnswerCard";

function Home() {
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);
  const [crossAnalysis, setCrossAnalysis] = useState("");

  return (
    <>
      <Navbar />

      <div className="home">
        <h1>CITEWISE AI</h1>

        <h3 className="hero-heading">
          Citation-Verified Research Assistant
        </h3>

        <p className="hero-subtitle">
          Upload research papers, ask intelligent questions,
          and receive reliable AI-generated answers backed by
          verified source citations.
        </p>

        <div className="hero-badges">
          <span>📄 PDF Analysis</span>
          <span>🔍 Source Citations</span>
          <span>⚖️ Conflict Detection</span>
        </div>

        {/* Upload + Chat Section */}
        <div className="top-section">
          <UploadCard />

          <ChatBox
            setAnswer={setAnswer}
            setSources={setSources}
            setCrossAnalysis={setCrossAnalysis}
          />
        </div>

        {/* AI Answer */}
        {answer && (
          <AnswerCard answer={answer} />
        )}

        {/* Source Citations */}
        <CitationPanel
          sources={sources}
        />

        {/* Cross Analysis */}
        <ConflictPanel
          analysis={crossAnalysis}
        />

      </div>
    </>
  );
}

export default Home;