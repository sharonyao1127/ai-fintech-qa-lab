from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Mock Payment Service")

users = {
    "user_001": {
        "eligibility_status": "approved",
        "payment_feature_status": "disabled",
        "balance": 1000,
    }
}

payments = {}


class PaymentRequest(BaseModel):
    request_id: str
    user_id: str
    amount: int
    transaction_id: str


@app.post("/payment-feature/enable")
def enable_payment_feature(user_id: str):
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user["eligibility_status"] != "approved":
        raise HTTPException(status_code=403, detail="User eligibility not approved")
    user["payment_feature_status"] = "enabled"
    return {"user_id": user_id, "payment_feature_status": "enabled"}


@app.post("/payments/process")
def process_payment(request: PaymentRequest):
    user = users.get(request.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user["payment_feature_status"] != "enabled":
        raise HTTPException(status_code=403, detail="Payment feature not enabled")

    # Idempotency by request_id.
    if request.request_id in payments:
        return {
            "status": "duplicate_ignored",
            "payment": payments[request.request_id],
        }

    if user["balance"] < request.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    user["balance"] -= request.amount
    record = {
        "request_id": request.request_id,
        "transaction_id": request.transaction_id,
        "user_id": request.user_id,
        "amount": request.amount,
        "status": "processed",
    }
    payments[request.request_id] = record
    return {"status": "processed", "payment": record}


@app.get("/balance/{user_id}")
def get_balance(user_id: str):
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id, "balance": user["balance"]}
