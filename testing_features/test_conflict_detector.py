from conflict_detector import detect_conflicts

def test_detects_conflict():
    chunks = [
        "The study found that the new method improves accuracy by 20%.",
        "The study found that the new method does not improve accuracy."
    ]
    conflicts = detect_conflicts(chunks)
    assert len(conflicts) == 1, f"Expected 1 conflict, got {len(conflicts)}"

def test_no_false_conflict():
    chunks = [
        "The experiment was conducted over 6 months.",
        "Data was collected from 50 participants."
    ]
    conflicts = detect_conflicts(chunks)
    assert len(conflicts) == 0, f"Expected 0 conflicts, got {len(conflicts)}"
