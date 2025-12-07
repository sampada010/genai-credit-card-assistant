# bot_ai/executor.py

def execute_action(intent: str):
    if intent == "block_card":
        return "Your card has been successfully blocked."

    if intent == "bill_summary":
        return "Unable to fetch bill summary at the moment."

    if intent == "convert_emi":
        return "Your amount has been converted to EMI."

    return None
