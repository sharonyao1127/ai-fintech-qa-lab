from dataclasses import dataclass
from typing import Any, Dict, List
import yaml


@dataclass
class RiskMatch:
    id: str
    name: str
    risk_level: str
    matched_keywords: List[str]
    impacted_areas: List[str]
    suggested_tests: List[str]
    monitoring_signals: List[str]


def load_risk_rules(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("rules", [])


def analyze_requirement(requirement: str, rules: List[Dict[str, Any]]) -> List[RiskMatch]:
    """Simple MVP risk analyzer based on keyword matching.

    Future versions can replace this with an LLM-based analyzer.
    """
    requirement_lower = requirement.lower()
    matches: List[RiskMatch] = []

    for rule in rules:
        keywords = rule.get("keywords", [])
        matched = [kw for kw in keywords if kw.lower() in requirement_lower]

        if matched:
            matches.append(
                RiskMatch(
                    id=rule["id"],
                    name=rule["name"],
                    risk_level=rule.get("risk_level", "medium"),
                    matched_keywords=matched,
                    impacted_areas=rule.get("impacted_areas", []),
                    suggested_tests=rule.get("suggested_tests", []),
                    monitoring_signals=rule.get("monitoring_signals", []),
                )
            )

    return matches
