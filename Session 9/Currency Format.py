def format_price(price,currency):
    if currency=='INR':
        return f"₹{price}"
    elif currency=='USD':
        return f"${price}"


print(format_price(500,"INR"))
print(format_price(500,"USD"))
