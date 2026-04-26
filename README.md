# AI Fintech QA Lab

AI Fintech QA Lab is an AI-assisted quality engineering project for generic fintech payment systems.

It demonstrates how a QA engineer can convert product requirements and structured payment risk rules into:

- risk-based test cases
- quality reports
- regression scope suggestions
- executable API checks against a mock payment service

## Why I Built This

Fintech payment systems involve complex reliability and fund-safety risks, including duplicate payment requests, delayed provider callbacks, user eligibility status mismatch, reward idempotency, asynchronous confirmation delays, and reconciliation gaps.

Traditional testing often depends heavily on manual experience. This project explores how AI-assisted workflows and structured risk rules can help QA engineers identify high-risk scenarios earlier and generate more reliable test assets.

This repository contains only generalized and sanitized scenarios. It does not include any company-specific business logic, internal APIs, production data, or confidential implementation details.

## Demo Flow

1. Input a generic payment requirement document.
2. Load structured payment risk rules.
3. Analyze impacted risk areas.
4. Generate risk-based test cases.
5. Generate a quality report.
6. Run API tests against a mock payment service.

## Project Structure

```text
ai-fintech-qa-lab/
├── examples/
│   └── requirements/
│       └── digital_payment_flow.md
├── risk_rules/
│   └── fintech_payment_risk_rules.yaml
├── src/
│   ├── main.py
│   ├── requirement_loader.py
│   ├── risk_analyzer.py
│   ├── testcase_generator.py
│   └── report_generator.py
├── mock_payment_service/
│   └── main.py
├── tests/
│   ├── test_risk_analyzer.py
│   └── test_duplicate_payment_request.py
├── outputs/
│   ├── generated_test_cases.md
│   └── quality_report.md
├── docs/
│   ├── architecture.md
│   └── roadmap.md
└── .github/
    └── workflows/
        └── test.yml
```

## Quick Start

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate test cases and quality report:

```bash
python -m src.main
```

Run tests:

```bash
pytest -q
```

Start mock payment service:

```bash
uvicorn mock_payment_service.main:app --reload
```

## Example Output

The project reads:

- `examples/requirements/digital_payment_flow.md`
- `risk_rules/fintech_payment_risk_rules.yaml`

Then generates:

- `outputs/generated_test_cases.md`
- `outputs/quality_report.md`

## Tech Stack

Python · Pytest · FastAPI · YAML · GitHub Actions · Risk-based Testing · AI-assisted QA

## Current Status

MVP version. The current implementation uses structured risk rules and keyword matching. Future versions can integrate LLM APIs for requirement understanding, test generation, and evaluation.
