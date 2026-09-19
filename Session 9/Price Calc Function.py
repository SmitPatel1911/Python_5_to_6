def calculate_final_price(price,discount_rate):
    discount=price*(discount_rate/100)
    final_price=price-discount
    return final_price


price=1000
discount_rate=20

print("Final Price : ",calculate_final_price(price,discount_rate))
