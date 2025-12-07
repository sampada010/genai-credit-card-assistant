import re
from typing import List, Tuple

KB_PATH = 'data/knowledge_base.md'


def load_kb() -> List[Tuple[str, str]]:
    with open(KB_PATH, 'r', encoding='utf-8') as f:
        text = f.read()

    parts = re.split(r'\n(?=#)', text)
    entries = []

    for part in parts:
        part = part.strip()
        if not part:
            continue

        lines = part.splitlines()
        heading = lines[0].lstrip('#').strip()
        body = '\n'.join(lines[1:]).strip()

        entries.append((heading, body))

    return entries


KB = load_kb()


def score_text(query: str, text: str) -> int:
    qwords = set(re.findall(r"\w+", query.lower()))
    twords = set(re.findall(r"\w+", text.lower()))
    return len(qwords & twords)


def search_info(query: str) -> str:
    best_score = -1
    best_section = None

    for heading, body in KB:
        s = score_text(query, heading + ' ' + body)
        if s > best_score:
            best_score = s
            best_section = (heading, body)

    if best_score <= 0:
        return "I couldn't find an exact answer. You can ask about billing, EMI, delivery, onboarding, or repayments."

    heading, body = best_section
    return f"**{heading}**\n\n{body}"
