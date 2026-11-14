# my_assistant.py
# Author: Mahendra Prashad


class ServiceAssistant:
    """A vehicle service assistant with rules, a tool, and an AI model."""

    def __init__(self, name, instructions, appointment_tool, model):
        """Store assistant details, tool, model, and conversation history."""
        self.name = name
        self.instructions = instructions
        self.appointment_tool = appointment_tool
        self.model = model
        self.history = []

    def respond(self, user_message):
        """Record the user's message and the assistant's reply."""
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
        """Use trusted rules first, then ask the model."""
        text = user_message.lower()

        if any(word in text for word in ["cancel", "reschedule", "change"]):
            return (
                "I can't change appointments here. "
                "I'm passing you to a human service advisor."
            )

        if any(word in text for word in ["appointment", "available", "open", "times"]):
            return self.appointment_reply(user_message)

        return self.model_reply()

    def model_reply(self):
        """Ask the model and return a safe reply if it cannot answer."""
        reply = self.model.reply(self.instructions, self.history)

        if reply is None:
            return (
                "Sorry, I can't answer that right now. "
                "Please try again in a moment."
            )

        return reply

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

