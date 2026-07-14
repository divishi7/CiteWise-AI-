import Navbar from "./Navbar";
import UploadCard from "./UploadCard";
import ChatBox from "./ChatBox";
import AnswerCard from "./AnswerCard";
import CitationPanel from "./CitationPanel";
import ConflictPanel from "./ConflictPanel";
function Home() {
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

        <div className="top-section">
    <UploadCard />
    <ChatBox />
</div>
   <AnswerCard />
   <CitationPanel />
   <ConflictPanel />
        
      </div>
    </>
  );
}

export default Home;