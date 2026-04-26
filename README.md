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
│   ├── requirements/
│   │   └── digital_payment_flow.md
│   └── openapi/
│       └── payment_api.yaml
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
│   ├── quality_report.md
│   └── coverage_matrix.md
├── docs/
│   ├── architecture.md
│   ├── roadmap.md
│   ├── risk-model.md
│   └── how-to-extend-rules.md
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
- `outputs/coverage_matrix.md`

## Tech Stack

Python · Pytest · FastAPI · YAML · GitHub Actions · Risk-based Testing · AI-assisted QA

## Current Status

MVP version. The current implementation uses structured risk rules and keyword matching. Future versions can integrate LLM APIs for requirement understanding, test generation, and evaluation. Future version can connect generated risk cases with OpenAPI contract coverage.

## Demo Output

After running:

```bash
python3 -m src.main
pytest -q
```

The project generates:

- `outputs/generated_test_cases.md`
- `outputs/quality_report.md`
- `outputs/coverage_matrix.md`

Example risk areas:

```text
- Duplicate Payment Request
- User Eligibility Status Consistency
- Reward Idempotency
- Async Confirmation Delay
```

Example test ideas:

```text
- Submit the same payment request twice.
- Simulate provider timeout followed by delayed success callback.
- Verify that user balance is deducted only once.
- Verify frontend/backend status consistency.
```

## Key Capabilities

- Converts generic payment requirements into risk-based test cases.
- Uses structured risk rules to identify high-risk payment scenarios.
- Generates quality reports with regression scope and monitoring signals.
- Provides a mock payment service for executable API testing.
- Verifies duplicate request handling with pytest.
- Uses GitHub Actions to run report generation and tests automatically.

## Interview Talking Points

I built this project to show how QA experience can be transformed into reusable testing assets.

The project takes a generic fintech payment requirement and structured risk rules as input, then generates risk-based test cases and a quality report. It also includes a mock payment service and pytest tests to prove that the testing ideas can become executable checks.

The key idea is not to replace QA judgment with AI, but to make QA judgment more structured, reusable, and automation-friendly.

This project demonstrates my experience in payment reliability, risk-based testing, API automation, idempotency, asynchronous processing, and AI-assisted quality engineering.
