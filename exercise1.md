# Exercise 1 — Label the Parts
Author: Mahendra Prashad
Course: ISM 3232

1. The two classes are:
   - OrderLookup
   - SupportChatbot

2. The one object of each class in main.py:
   - order_tool (OrderLookup object)
   - bot (SupportChatbot object)

3. Every attribute of SupportChatbot:
   - self.name
   - self.instructions
   - self.order_tool
   - self.history

4. Every method of OrderLookup:
   - __init__()
   - find_order_id()
   - find_status()

5. The line in chatbot.py that is the composition:
   self.order_tool = order_tool

6. In bot.respond("Hello"), self is:
   - The bot object, an instance of SupportChatbot.