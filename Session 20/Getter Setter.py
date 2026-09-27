class Product:

    def __init__(self,name,price):
        self.name=name
        self._price=price

    def get_price(self):
        return self._price

    def set_price(self,price):
        self._price=price

p1=Product("Wireless Headphones", 1999)
print("Current Price : Rs.",p1.get_price())
p1.set_price(1799)
print("Updated Price : Rs.",p1.get_price())
