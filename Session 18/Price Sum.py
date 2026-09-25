import re

text="Pizza-Rs.399 , Burger-Rs.159, Sandwich-Rs.299, Fries-Rs.99"

prices=re.findall(r"Rs\.(\d+)",text)
prices=[int(price) for price in prices]

print("Prices : ",prices)
print("Sum : ",sum(prices))
