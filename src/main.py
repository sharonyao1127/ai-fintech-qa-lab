from pathlib import Path

from src.requirement_loader import load_requirement
from src.risk_analyzer import analyze_requirement, load_risk_rules
from src.testcase_generator import generate_test_cases
from src.report_generator import generate_quality_report


ROOT = Path(__file__).resolve().parents[1]
REQUIREMENT_PATH = ROOT / "examples" / "requirements" / "digital_payment_flow.md"
RULES_PATH = ROOT / "risk_rules" / "fintech_payment_risk_rules.yaml"
OUTPUT_DIR = ROOT / "outputs"


def main() -> None:
    requirement = load_requirement(str(REQUIREMENT_PATH))
    rules = load_risk_rules(str(RULES_PATH))
    matches = analyze_requirement(requirement, rules)

    OUTPUT_DIR.mkdir(exist_ok=True)

    test_cases = generate_test_cases(matches)
    report = generate_quality_report(matches)

    (OUTPUT_DIR / "generated_test_cases.md").write_text(test_cases, encoding="utf-8")
    (OUTPUT_DIR / "quality_report.md").write_text(report, encoding="utf-8")

    print(f"Generated {len(matches)} matched risk areas.")
    print(f"- {OUTPUT_DIR / 'generated_test_cases.md'}")
    print(f"- {OUTPUT_DIR / 'quality_report.md'}")


if __name__ == "__main__":
    main()
