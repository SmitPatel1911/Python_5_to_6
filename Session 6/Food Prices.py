food_prices={"Pizza":250,"Burger":189,"Pasta":210,"Sandwich":350,"Noodles":160}

for item, price in food_prices.items():
    if price > 200:
        print("Item : ",item,"Price : ",price)
