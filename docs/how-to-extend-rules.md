# How to Extend Risk Rules

To add a new risk rule:

1. Add a new rule in `risk_rules/fintech_payment_risk_rules.yaml`.
2. Define keywords, risk level, impacted areas, suggested tests, and monitoring signals.
3. Add or update requirement examples.
4. Run:

```bash
python3 -m src.main
pytest -q
```

Review generated outputs.
