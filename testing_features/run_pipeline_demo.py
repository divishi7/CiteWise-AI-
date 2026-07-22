import json

from utils import clean_chunk
from citation_verifier import verify_answer
from conflict_detector import detect_conflicts
from evaluator import citation_accuracy

with open("latest_run.json") as f:
    data = json.load(f)

raw_chunks = data["chunks"]
generated_answer = data["answer"]


chunks = [clean_chunk(c) for c in raw_chunks]

citation_results = verify_answer(chunks, generated_answer)
conflict_results = detect_conflicts(chunks)

print("=== Citation Check ===")
for r in citation_results:
    print(f"{r['label']} ({r['confidence']:.2f}): {r['claim']}")

print("=== Conflicts ===")
for c in conflict_results:
    print(f"CONFLICT (confidence {c['confidence']:.2f}):")
    print(f"  A: {c['chunk_a']}")
    print(f"  B: {c['chunk_b']}")
    print()

accuracy = citation_accuracy(citation_results)

print(f"\nCitation accuracy: {citation_accuracy(citation_results):.1%}")
