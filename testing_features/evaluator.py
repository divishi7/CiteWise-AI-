def citation_accuracy(results):
    """Returns the % of claims that were supported (entailment) out of all claims checked."""
    if not results:
        return 0.0
    supported = sum(1 for r in results if r["label"] == "entailment")
    return supported / len(results)
