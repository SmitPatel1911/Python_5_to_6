class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price

    def get_discounted_price(self):
        return self.price*0.90 

class Electronics(Product):
    def get_discounted_price(self):
        return self.price*0.80  

product=Product("T-Shirt",1000)
electronic=Electronics("Laptop",50000)
print("Product:",product.name)
print("Original Price : ",product.price)
print("Discounted Price: ₹",product.get_discounted_price())
print("* "*30)
print("Electronics : ", electronic.name)
print("Original Price : ",electronic.price)
print("Discounted Price: Rs.",electronic.get_discounted_price())
