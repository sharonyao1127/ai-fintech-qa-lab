from typing import List
from src.risk_analyzer import RiskMatch


def generate_test_cases(matches: List[RiskMatch]) -> str:
    lines = ["# Generated Risk-based Test Cases", ""]

    if not matches:
        lines.extend([
            "No risk areas were matched.",
            "",
            "Please review the requirement manually or add more risk rules.",
        ])
        return "\n".join(lines)

    for match in matches:
        lines.extend([
            f"## Risk Area: {match.name}",
            "",
            f"**Risk Level:** {match.risk_level}",
            "",
            "### Matched Keywords",
            "",
            ", ".join(match.matched_keywords),
            "",
            "### Impacted Areas",
            "",
        ])

        for area in match.impacted_areas:
            lines.append(f"- {area}")

        lines.extend(["", "### Suggested Test Cases", ""])

        for idx, test in enumerate(match.suggested_tests, start=1):
            lines.append(f"{idx}. {test}")

        lines.append("")

    return "\n".join(lines)
