from typing import List
from src.risk_analyzer import RiskMatch


def generate_quality_report(matches: List[RiskMatch]) -> str:
    lines = [
        "# Quality Report",
        "",
        "## Risk Summary",
        "",
        "| Risk Area | Level | Matched Keywords |",
        "|---|---|---|",
    ]

    if not matches:
        lines.append("| No matched risk | N/A | N/A |")
    else:
        for match in matches:
            lines.append(
                f"| {match.name} | {match.risk_level} | {', '.join(match.matched_keywords)} |"
            )

    lines.extend(["", "## Suggested Regression Scope", ""])

    if not matches:
        lines.append("- Manual review required.")
    else:
        seen = set()
        for match in matches:
            for area in match.impacted_areas:
                if area not in seen:
                    seen.add(area)
                    lines.append(f"- {area}")

    lines.extend(["", "## Monitoring Signals", ""])

    if not matches:
        lines.append("- No monitoring signals generated.")
    else:
        signals = []
        for match in matches:
            signals.extend(match.monitoring_signals)
        for signal in sorted(set(signals)):
            lines.append(f"- {signal}")

    return "\n".join(lines)
