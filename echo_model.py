# echo_model.py
# Author: Mahendra Prashad


class EchoModel:
    """A simple model that repeats the user's last message."""

    def reply(self, instructions, history):
        """Return 'You said:' followed by the last message."""
        return "You said: " + history[-1]["content"]