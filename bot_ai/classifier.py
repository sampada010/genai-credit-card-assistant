# bot_ai/classifier.py
def classify_intent(message: str):
    msg = message.lower()

    if "block" in msg and "card" in msg:
        return "block_card"

    if "bill" in msg or "statement" in msg:
        return "bill_summary"

    if "emi" in msg or "installment" in msg:
        return "convert_emi"

    return "general"
