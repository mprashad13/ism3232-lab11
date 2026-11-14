# my_main.py
# Author: Mahendra Prashad

from my_assistant import ServiceAssistant
from my_tool import AppointmentLookup
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Alex, a friendly vehicle service appointment assistant.
Answer customer questions in one short sentence.
You can help customers check available service appointment times.
Appointment changes and cancellations must be handled by a human service advisor.
Do not invent appointment times, prices, or service policies.
If you do not know an answer, say you do not know and offer to connect
the customer with a human service advisor."""

APPOINTMENTS = {
    "Monday": ["9:00 AM", "2:30 PM"],
    "Wednesday": ["10:00 AM", "3:00 PM"],
    "Friday": ["8:30 AM", "1:00 PM"],
}

appointment_tool = AppointmentLookup(APPOINTMENTS)
model = OllamaModel(MODEL_NAME)

assistant = ServiceAssistant(
    "Alex",
    INSTRUCTIONS,
    appointment_tool,
    model,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")

while user_message.strip().lower() != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")

