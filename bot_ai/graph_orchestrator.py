# bot_ai/graph_orchestrator.py
from bot_ai.classifier import classify_intent
from bot_ai.executor import execute_action
from bot_ai.retriever import retrieve
from bot_ai.generator import generate_answer


def handle_message(user_msg: str):
    intent = classify_intent(user_msg)

    # If it's an action, execute directly
    action_result = execute_action(intent)
    if action_result:
        return action_result

    # Otherwise → retrieve + generate
    docs = retrieve(user_msg, top_k=4)
    answer = generate_answer(user_msg, docs)
    return answer
