# my_assistant.py
# Author: Mahendra Prashad


class ServiceAssistant:
    """A rule-based vehicle service appointment assistant."""

    def __init__(self, name, instructions, appointment_tool):
        """Store assistant details, tool, and conversation history."""
        self.name = name
        self.instructions = instructions
        self.appointment_tool = appointment_tool
        self.history = []

    def respond(self, user_message):
        """Record the conversation and return a reply."""
        self.history.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        reply = self.choose_reply(user_message)

        self.history.append(
            {
                "role": "assistant",
                "content": reply,
            }
        )

        return reply

    def choose_reply(self, user_message):
        """Choose a response using simple keyword rules."""
        text = user_message.lower()

        if any(word in text for word in ["cancel", "reschedule", "change"]):
            return (
                "I can't change appointments here. "
                "I'm passing you to a human service advisor."
            )

        if any(word in text for word in ["appointment", "available", "open", "times"]):
            return self.appointment_reply(user_message)

        if "hello" in text:
            return (
                f"Hello! I'm {self.name}. "
                "I can check available service appointment times."
            )

        return (
            "I'm not sure how to help with that. "
            "I can check available appointment times."
        )

    def appointment_reply(self, user_message):
        """Use the appointment tool to check available times."""
        day = self.appointment_tool.find_day(user_message)

        if day is None:
            return "Which day? I can check Monday, Wednesday, or Friday."

        times = self.appointment_tool.find_times(day)

        if not times:
            return f"No appointment times are available on {day}."

        available = " and ".join(times)
        return f"Available times on {day}: {available}."
