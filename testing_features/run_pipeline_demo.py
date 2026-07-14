raw_chunks = [...]        # real list of strings from Member 2
generated_answer = "..."  # real string from Member 3

# Clean the chunks first
chunks = [clean_chunk(c) for c in raw_chunks]

# Run both of your functions
citation_results = verify_answer(chunks, generated_answer)
conflict_results = detect_conflicts(chunks)

print("=== Citation Check ===")
for r in citation_results:
    print(r["label"], "-", r["claim"])

print("=== Conflicts ===")
for c in conflict_results:
    print(c)
