#to verify claims
def verify_claim(chunk, claim):
    """Check if `chunk` supports `claim`. Returns entailment/contradiction/neutral + confidence."""
    scores = nli_model.predict([(chunk, claim)])
    label = LABELS[scores.argmax()]
    confidence = scores.max()
    return {"claim": claim, "chunk": chunk, "label": label, "confidence": confidence}

#to verify answers
def verify_answer(chunks, answer_text):
    """Check every claim in the answer against all chunks. Returns one result per claim."""
    results = []
    for claim in split_into_claims(answer_text):
        # check this claim against every chunk, keep the best match
        best_result = None
        for chunk in chunks:
            result = verify_claim(chunk, claim)
            if best_result is None or result["confidence"] > best_result["confidence"]:
                best_result = result
        results.append(best_result)
    return results
