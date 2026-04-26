# Architecture

## MVP Architecture

```text
Requirement Markdown
        |
        v
Risk Rule YAML
        |
        v
Risk Analyzer
        |
        +--> Generated Test Cases
        |
        +--> Quality Report
        |
        +--> Suggested Regression Scope
```

## Design Notes

The MVP uses keyword matching to simulate AI-assisted requirement analysis.

Future versions can integrate LLMs for:

- semantic requirement understanding
- test case generation
- risk classification
- hallucination checks
- test coverage evaluation
