from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Mock Credit Card APIs")


class BlockCardRequest(BaseModel):
    user_id: str


class ConvertEmiRequest(BaseModel):
    transaction_id: str
    tenure_months: int


@app.post('/block-card')
async def block_card(req: BlockCardRequest):
    return {
        "message": f"Your card for user {req.user_id} has been blocked successfully."
    }


@app.post('/convert-emi')
async def convert_emi(req: ConvertEmiRequest):
    monthly = round((12000 / req.tenure_months) + 50)
    return {
        "monthly_emi": monthly,
        "tenure_months": req.tenure_months
    }


@app.get('/bill')
async def get_bill(user_id: str):
    return {
        "total_due": 4750,
        "minimum_due": 475,
        "due_date": "2025-12-20"
    }


@app.get('/')
async def root():
    return {"message": "Mock API Running"}
