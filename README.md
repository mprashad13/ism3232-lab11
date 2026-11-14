ISM 3232 — Lab 10: OOP for Agents

Author: Mahendra Prashad

Mini-Project: Vehicle Service Appointment Assistant

My mini-project is a vehicle service appointment assistant named Alex that helps customers check available service appointment times. The assistant uses a separate AppointmentLookup class to retrieve appointment information and maintains a conversation history for each interaction. This project is a simulation that uses fictional appointment schedules rather than real dealership scheduling systems or customer information. Requests involving appointment cancellations, rescheduling, or changes are directed to a human service advisor because those actions require authorization and access to actual scheduling records. If this system were connected to real customer information, a potential risk would be exposing personal details or providing inaccurate appointment availability. Proper authentication, data protection, and integration with an updated scheduling system would be necessary before using this assistant in a real business environment.

Week 11 — Local AI Models and Conversation Memory

Overview

In Week 11, I upgraded my chatbot to use a local AI model through Ollama. I installed Granite 4.1 3B and connected it to Python.

Changes Made

Created MockModel to test chatbot responses without Ollama.

Created OllamaModel to communicate with the local AI model.

Updated SupportChatbot to use rules for orders, inventory, and human handoffs.

Upgraded my vehicle service appointment assistant to use an AI model.

Preserved appointment lookup functionality and human handoff rules.

Added a safe fallback response when the model is unavailable.

What I Learned

I learned how to connect a Python application to a local AI model and manage conversation history. I also learned why important business rules should be handled by Python rather than relying entirely on AI-generated responses.

Testing

I used pytest to verify that my chatbot and vehicle service assistant work correctly. All 20 tests passed.

Reflection

The biggest challenge was updating the existing assistant and its tests to accept the new model argument. I resolved this by updating the constructor calls and using MockModel for testing. This helped me understand how AI models can be integrated into existing Python applications without losing their original functionality.