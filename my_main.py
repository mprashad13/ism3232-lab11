# my_main.py
# Author: Mahendra Prashad

from my_assistant import ServiceAssistant
from my_tool import AppointmentLookup

APPOINTMENTS = {
    "Monday": ["9:00 AM", "2:30 PM"],
    "Wednesday": ["10:00 AM", "3:00 PM"],
    "Friday": ["8:30 AM", "1:00 PM"],
}

appointment_tool = AppointmentLookup(APPOINTMENTS)

assistant = ServiceAssistant(
    "Alex",
    "You are a friendly vehicle service appointment assistant.",
    appointment_tool,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")

while user_message.lower() != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
