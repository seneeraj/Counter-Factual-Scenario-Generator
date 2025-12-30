import re

def validate_dse_output(text: str) -> bool:
    """
    Returns True if output satisfies DSE constraints.
    """

    # Rule 1: Must have exactly 10 numbered items
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    numbered = [l for l in lines if re.match(r"^\d+\.", l)]

    if len(numbered) != 10:
        return False

    # Rule 2: At least 7 must start with What if / Why not
    starters = sum(
        l.lower().startswith(("what if", "why not"))
        for l in numbered
    )
    if starters < 7:
        return False

    # Rule 3: No question marks allowed (no interrogative framing)
    if "?" in text:
        return False

    # Rule 4: Reject obvious domain drift
    forbidden_domains = [
        "art", "food", "religion", "education",
        "renaissance", "roman", "empire", "medieval"
    ]
    lowered = text.lower()
    if any(word in lowered for word in forbidden_domains):
        return False

    # Rule 5: Cultural drift must be treated as a process
    process_terms = [
        "rate", "accelerat", "slow", "lock",
        "irreversible", "revers", "selection",
        "feedback", "drift"
    ]
    if not any(term in lowered for term in process_terms):
        return False

    return True
