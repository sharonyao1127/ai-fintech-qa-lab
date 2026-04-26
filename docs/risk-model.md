# Risk Model

This project focuses on common fintech payment quality risks.

## Core Risk Categories

### 1. Idempotency

Duplicate requests should not create duplicate balance deduction, reward issuance, or transaction records.

### 2. State Consistency

Frontend status, backend status, and provider status should remain consistent across async processing.

### 3. Async Confirmation

External provider callbacks may arrive late, duplicate, or out of order.

### 4. Reconciliation

Transaction records and external confirmations should be reconciled to detect mismatch, missing confirmation, or long-pending states.

### 5. Reward / Campaign Logic

Reward-related logic should be protected against duplicate trigger, boundary conditions, and eligibility mismatch.
