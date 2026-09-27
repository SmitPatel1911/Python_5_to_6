class FoodOrder():

    def order(self,name,items,price):
        self.name=name
        self.items=items
        self.price=price
    def print(self):
        print("Restaurant : ",self.name)
        print("Items : ",self.items)
        print("Total : ",self.price)
        
l1=FoodOrder()
l1.order("Domino's",["Farmhouse Pizza","Garlic Bread","Coke"],699)
l1.print()
