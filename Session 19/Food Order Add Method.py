class FoodOrder():

    def order(self,name,items,price):
        self.name=name
        self.items=items
        self.price=price
    def print(self):
        print("Restaurant : ",self.name)
        print("Items : ",self.items)
        print("Total : ",self.price)
    def add_items(self,item_name,item_price):
        self.items.append(item_name)
        self.price+=item_price
        
l1=FoodOrder()
l1.order("Domino's",["Farmhouse Pizza","Garlic Bread","Coke"],699)
l1.add_items("Choco Lava Cake",199)
l1.add_items("Paneer Stuffed Garlic Bread",209)
l1.print()
