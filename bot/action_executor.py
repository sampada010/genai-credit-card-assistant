import requests

MOCK_BASE = 'http://127.0.0.1:8000'


def execute_action(intent: str, user_id: str = 'user_123', **kwargs):
    if intent == 'block_card':
        payload = {'user_id': user_id}
        if 'card_id' in kwargs:
            payload['card_id'] = kwargs['card_id']

        r = requests.post(f"{MOCK_BASE}/block-card", json=payload)
        return r.json().get('message', 'Action failed.')

    if intent == 'convert_emi':
        payload = {
            'transaction_id': kwargs.get('transaction_id', 'txn_001'),
            'tenure_months': kwargs.get('tenure_months', 6)
        }

        r = requests.post(f"{MOCK_BASE}/convert-emi", json=payload)
        body = r.json()
        return f"EMI created. ₹{body.get('monthly_emi')} per month for {body.get('tenure_months')} months."

    if intent == 'get_bill':
        r = requests.get(f"{MOCK_BASE}/bill", params={'user_id': user_id})
        body = r.json()
        return f"Your total due is ₹{body.get('total_due')}, minimum due is ₹{body.get('minimum_due')}, due date {body.get('due_date')}."

    return None
