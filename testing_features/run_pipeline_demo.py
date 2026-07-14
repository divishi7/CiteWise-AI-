from utils import clean_chunk
from citation_verifier import verify_answer
from conflict_detector import detect_conflicts

# 🔧 Replace these two lines with real data from Member 2 and Member 3
raw_chunks = [...]        # list of strings — from Member 2
generated_answer = "..."  # one string — from Member 3

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
