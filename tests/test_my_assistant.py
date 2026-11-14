# tests/test_my_assistant.py
# Author: Mahendra Prashad

from mock_model import MockModel
from my_assistant import ServiceAssistant
from my_tool import AppointmentLookup


def make_assistant():
    """Create a fresh assistant and appointment tool for each test."""
    appointments = {
        "Monday": ["9:00 AM", "2:30 PM"],
        "Wednesday": ["10:00 AM", "3:00 PM"],
        "Friday": ["8:30 AM", "1:00 PM"],
    }
    tool = AppointmentLookup(appointments)
    return ServiceAssistant("Alex", "Be friendly.", tool, MockModel())



def test_appointment_lookup():
    """Test that the assistant uses the appointment tool."""
    assistant = make_assistant()
    reply = assistant.respond("What times are open on Monday?")
    assert reply == "Available times on Monday: 9:00 AM and 2:30 PM."


def test_unknown_day():
    """Test that an unknown day receives a helpful reply."""
    assistant = make_assistant()
    reply = assistant.respond("What appointments are available?")
    assert "Which day?" in reply


def test_human_handoff():
    """Test that rescheduling requests go to a human."""
    assistant = make_assistant()
    reply = assistant.respond("Can you reschedule my appointment?")
    assert "human service advisor" in reply


def test_unknown_request():
    """Test that unrelated requests receive a safe response."""
    assistant = make_assistant()
    reply = assistant.respond("Do you validate parking?")
    assert "not sure" in reply


def test_conversation_history():
    """Test that user and assistant messages are recorded."""
    assistant = make_assistant()
    assistant.respond("hello")
    assistant.respond("What times are open on Monday?")

    assert len(assistant.history) == 4
    assert assistant.history[0]["role"] == "user"
    assert assistant.history[1]["role"] == "assistant"
    assert assistant.history[2]["role"] == "user"
    assert assistant.history[3]["role"] == "assistant"
