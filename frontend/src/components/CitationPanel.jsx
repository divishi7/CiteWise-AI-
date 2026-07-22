import "./CitationPanel.css";

function CitationPanel({ sources = [] }) {

  return (

    <div className="citation-panel">

      <h2>📚 Sources Used</h2>

      {sources.length === 0 ? (

        <div className="citation-card">
          <p>No citations yet.</p>
        </div>

      ) : (

        sources.map((source, index) => (

          <div className="citation-card" key={index}>

            <div className="citation-top">

              <span className="page-badge">
                📄 Page {source.page}
              </span>

              <span className="match-badge high">
                Source
              </span>

            </div>

            <p>
              <strong>{source.source}</strong>
            </p>

            <p>
              Chunk ID: {source.chunk_id}
            </p>

          </div>

        ))

      )}

    </div>

  );

}

export default CitationPanel;