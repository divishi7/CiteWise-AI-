# Testing & Advanced Features Module

## What it does
This module verifies whether generated answers are supported by retrieved
document chunks (citation verification), and detects contradictions between
different source documents (conflict detection). Built using an NLI model
from Hugging Face (cross-encoder/nli-deberta-v3-base).

## How to run
1. Install dependencies: pip install -r requirements.txt
2. For citation checking: call verify_answer(chunks, answer_text)
3. For conflict detection: call detect_conflicts(chunks)
4. See run_pipeline_demo.py for a full example

## Metrics
- Citation accuracy: [your real number from evaluator.py]%
- Conflicts detected in demo dataset: [your real number]

## Known limitations
- Sentence splitting is basic (regex-based) and may mis-split some abbreviations
- Confidence threshold (0.6) was tuned manually on a small sample, not a large labeled dataset
- Conflict detection compares every pair of chunks, which would be slow on very large documents
