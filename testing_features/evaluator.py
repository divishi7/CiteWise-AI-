def citation_accuracy(results):
    """Returns % of claims that were NOT contradicted (entailment + neutral both count as acceptable).
    Contradiction is treated as the real red flag — an actual hallucination/mismatch signal."""
    if not results:
        return 0.0
    not_contradicted = sum(1 for r in results if r["label"] != "contradiction")
    return not_contradicted / len(results)
