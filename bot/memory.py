class ConversationMemory:
    """
    Simple in-memory conversation history.
    Stores the last N messages to provide context.
    """

    def __init__(self, max_length=5):
        self.max_length = max_length
        self.messages = []

    def add(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})
        if len(self.messages) > self.max_length:
            self.messages.pop(0)

    def get_history(self):
        """Return messages in conversational order."""
        return self.messages

    def clear(self):
        self.messages = []


# Global memory object (simple + works for prototype)
memory = ConversationMemory()
