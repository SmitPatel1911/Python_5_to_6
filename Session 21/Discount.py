class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def get_discounted_price(self):
        return self.price*0.90


product=Product("Wireless Headphones",2000)

print("Product : ",product.name)
print("Original Price : Rs.",product.price)
print("Discounted Price : Rs.",product.get_discounted_price())
