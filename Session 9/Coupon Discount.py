def apply_coupon(price,coupon_code=None):
    if coupon_code=="ZOMATO10":
        discount=price*0.10
        return price-discount
    else:
        return price


print(apply_coupon(500,"ZOMATO10"))
print(apply_coupon(500))
print(apply_coupon(500,"ABC123"))
