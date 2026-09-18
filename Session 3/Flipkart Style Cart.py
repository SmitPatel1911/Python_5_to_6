def total_cart_amount(prices):
    total=0.0
    for i in prices:
        total+=float(i)
    return total


cart=['199.99', '49', '350.75']

result=total_cart_amount(cart)
print("Total cart amount: Rs.",result)
    
