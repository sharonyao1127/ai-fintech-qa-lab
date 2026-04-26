# Requirement: Digital Payment Flow

Users who meet platform eligibility requirements can enable a digital payment feature.

After the payment feature is enabled, users can complete transactions using their available account balance.

When a payment request is sent to an external payment provider, the system should reserve the required amount and wait for the provider response.

If the payment request times out, the system should wait for the delayed provider callback and must avoid duplicate balance deduction.

If the provider callback is duplicated or retried, the system should guarantee idempotency.

After the transaction is completed, users may receive a campaign reward according to platform rules.

The frontend payment status should remain consistent with backend processing status, especially when user eligibility changes or payment enablement fails.
