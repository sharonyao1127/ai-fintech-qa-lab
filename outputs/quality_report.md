# Quality Report

## Risk Summary

| Risk Area | Level | Matched Keywords |
|---|---|---|
| Duplicate Payment Request | high | payment request, callback, duplicate, reserve |
| User Eligibility Status Consistency | high | eligibility, frontend, backend, status |
| Reward Idempotency | medium | reward, campaign, completed, duplicate, transaction |
| Async Confirmation Delay | high | delayed, completed |

## Suggested Regression Scope

- idempotency
- balance deduction
- transaction record
- external provider callback
- reconciliation
- user eligibility
- payment feature enablement
- frontend/backend consistency
- compliance state
- reward calculation
- campaign eligibility
- compensation
- user balance
- transaction status
- provider confirmation
- user-facing payment status

## Monitoring Signals

- Abnormal payment / confirmation mismatch
- Abnormal reward amount
- Callback retry spike
- Duplicate reward record
- Duplicate transaction ID
- Eligibility status mismatch
- Inconsistent frontend/backend status
- Long pending confirmation
- Missing provider confirmation record
- Multiple transaction records with same request ID
- Payment enablement failures by eligibility state
- Payment/confirmation amount mismatch
- Reward issued for ineligible transaction