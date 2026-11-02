# stock_tool.py
# Author: Mahendra Prashad


class StockLookup:
    """A tool for checking product inventory."""

    def __init__(self, products):
        """Store product names and their stock status."""
        self.products = products

    def find_product(self, text):
        """Find a known product mentioned in the message."""
        for product in self.products:
            if product.lower() in text.lower():
                return product
        return None

    def find_stock(self, product):
        """Return the stock status of a product."""
        return self.products.get(product)
