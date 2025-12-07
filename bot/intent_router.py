from typing import Dict

KEYWORD_INTENTS = {
    'block_card': ['block my card', 'block card', 'lost card', 'stolen card', 'disable card'],
    'convert_emi': ['convert to emi', 'emi', 'convert emi', 'make emi'],
    'get_bill': ['bill', 'statement', 'due', 'minimum due', 'total due'],
    'delivery_status': ['delivery', 'arrive', 'tracking', 'card delivery'],
}


def route_intent(user_message: str) -> Dict[str, str]:
    msg = user_message.lower()

    for intent, phrases in KEYWORD_INTENTS.items():
        for phrase in phrases:
            if phrase in msg:
                return {'intent': intent, 'confidence': 'high'}

    return {'intent': 'information', 'confidence': 'low'}
