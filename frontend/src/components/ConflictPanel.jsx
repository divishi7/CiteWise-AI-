import "./ConflictPanel.css";

function ConflictPanel() {
  const conflicts = [
    {
      title: "📘 Research Paper A",
      className: "paper-a",
      text: "Large Language Models require extremely large datasets for effective training and better generalization across tasks."
    },
    {
      title: "📙 Research Paper B",
      className: "paper-b",
      text: "Smaller domain-specific language models can achieve comparable performance while requiring significantly fewer computational resources."
    }
  ];

  return (
    <div className="conflict-panel">

      <h2>⚖️ Cross-Source Analysis</h2>

      <p className="conflict-subtitle">
        The uploaded documents present different perspectives on the same topic.
      </p>

      {conflicts.map((item, index) => (
        <div className={`conflict-card ${item.className}`} key={index}>

          <div className="source-title">
            {item.title}
          </div>

          <p>{item.text}</p>

        </div>
      ))}

      <div className="summary-box">

        <h3>🧠 AI Interpretation</h3>

        <p>
          Both papers explore the same research problem but recommend
          different approaches. One emphasizes scalability using
          large foundation models, while the other prioritizes
          efficiency through smaller domain-specific architectures.
        </p>

      </div>

    </div>
  );
}

export default ConflictPanel;