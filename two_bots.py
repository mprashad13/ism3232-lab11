# two_bots.py
# Author: Mahendra Prashad

from chatbot import SupportChatbot
from order_tool import OrderLookup
from stock_tool import StockLookup

orders = {"A100": "shipped", "A101": "processing"}
products = {"rain jacket": 12, "backpack": 5}

order_tool = OrderLookup(orders)
stock_tool = StockLookup(products)

sunny = SupportChatbot(
    "Sunny",
    "You are cheerful and brief.",
    order_tool,
    stock_tool,
)

river = SupportChatbot(
    "River",
    "You are formal and detailed.",
    order_tool,
    stock_tool,
)

sunny_reply = sunny.respond("hello")

river.respond("hello")
river_reply = river.respond("Where is order A100?")

print(sunny.name, len(sunny.history))
print(river.name, len(river.history))
print(sunny_reply)
print(river_reply)
print(sunny.instructions)
print(river.instructions)
