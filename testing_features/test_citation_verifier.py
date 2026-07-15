from citation_verifier import verify_claim

def test_clear_entailment():
    chunk = "RAG combines a retriever with a generator to reduce hallucination."
    claim = "RAG reduces hallucination by combining retrieval and generation."
    result = verify_claim(chunk, claim)
    assert result["label"] == "entailment", f"Expected entailment, got {result['label']}"

def test_clear_contradiction():
    chunk = "The system requires an internet connection to function."
    claim = "The system works completely offline."
    result = verify_claim(chunk, claim)
    assert result["label"] == "contradiction", f"Expected contradiction, got {result['label']}"

def test_unrelated_neutral():
    chunk = "The sky is blue."
    claim = "The system has 85% retrieval accuracy."
    result = verify_claim(chunk, claim)
    assert result["label"] == "neutral", f"Expected neutral, got {result['label']}"
