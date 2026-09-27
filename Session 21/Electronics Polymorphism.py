class Product:
    
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def get_discounted_price(self):
        return self.price*0.90 

class Electronics(Product):
    def get_discounted_price(self):
        return self.price*0.80 

def show_final_price(item):
    print("Product : ",item.name)
    print("Original Price : ",item.price)
    print("Discounted Price : Rs.",item.get_discounted_price())

product=Product("T-Shirt", 1000)
laptop=Electronics("Laptop", 50000)
show_final_price(product)
print("* "*30)
show_final_price(laptop)
