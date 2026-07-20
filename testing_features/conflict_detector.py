import itertools
import re
from sentence_transformers import CrossEncoder


from citation_verifier import nli_model, LABELS

def detect_conflicts(chunks):
    conflicts = []
    for chunk_a, chunk_b in itertools.combinations(chunks, 2):  # every unique pair
        scores = nli_model.predict([(chunk_a, chunk_b)], apply_softmax=True)
        label = LABELS[scores.argmax()]
        if label == "contradiction":
            conflicts.append({"chunk_a": chunk_a, "chunk_b": chunk_b, "confidence": scores.max()})
    return conflicts
