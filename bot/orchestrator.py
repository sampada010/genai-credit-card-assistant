from .intent_router import route_intent
from .retrieval import search_info
from .action_executor import execute_action
from .memory import memory
import re


def process_message(message: str, user_id: str = 'user_123') -> str:
    """
    Main function that processes user input and decides whether
    to retrieve information or execute an action via mock APIs.
    """

    # Save user message in memory
    memory.add("user", message)

    # Classify the intent
    route = route_intent(message)
    intent = route['intent']
    confidence = route['confidence']

    # If it's informational OR intent confidence is low -> use knowledge base
    if intent == 'information' or confidence == 'low':
        answer = search_info(message)

    else:
        # Handle actionable intents
        if intent == 'convert_emi':
            # Try detecting tenure like "6 months"
            match = re.search(r"(\d+)\s*(months|month|m)", message.lower())
            tenure = int(match.group(1)) if match else 6

            answer = execute_action(
                intent,
                user_id=user_id,
                transaction_id="txn_demo_001",
                tenure_months=tenure
            )

        else:
            # Block card, get bill, etc.
            answer = execute_action(intent, user_id=user_id)

    # Save assistant response in memory
    memory.add("assistant", answer)

    return answer
