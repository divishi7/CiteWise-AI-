import "./CitationPanel.css";

function CitationPanel() {

  const citations = [
    {
      page: 3,
      confidence: "High Match",
      text: "Large Language Models are trained on massive datasets to understand natural language."
    },
    {
      page: 7,
      confidence: "High Match",
      text: "Transformer architecture enables contextual understanding through attention mechanisms."
    },
    {
      page: 12,
      confidence: "Medium Match",
      text: "Embeddings convert text into numerical vectors for semantic search."
    }
  ];

  return (

    <div className="citation-panel">

      <h2>📚 Sources Used</h2>

      {citations.map((citation, index) => (

        <div className="citation-card" key={index}>

          <div className="citation-top">

            <span className="page-badge">
              📄 Page {citation.page}
            </span>

            <span
              className={`match-badge ${
                citation.confidence === "High Match"
                  ? "high"
                  : "medium"
              }`}
            >
              {citation.confidence}
            </span>

          </div>

          <p>{citation.text}</p>

        </div>

      ))}

    </div>

  );

}

export default CitationPanel;