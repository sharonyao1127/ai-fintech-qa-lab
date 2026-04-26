from src.risk_analyzer import analyze_requirement


def test_analyze_requirement_matches_duplicate_payment_request():
    requirement = "Payment request may timeout and provider callback can be duplicated."
    rules = [
        {
            "id": "duplicate_payment_request",
            "name": "Duplicate Payment Request",
            "keywords": ["payment request", "timeout", "callback", "duplicate"],
            "risk_level": "high",
            "impacted_areas": ["idempotency"],
            "suggested_tests": ["Submit duplicated payment request."],
            "monitoring_signals": ["Duplicate transaction ID"],
        }
    ]

    matches = analyze_requirement(requirement, rules)

    assert len(matches) == 1
    assert matches[0].id == "duplicate_payment_request"
    assert "payment request" in matches[0].matched_keywords
