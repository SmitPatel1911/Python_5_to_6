def order_id_generator():
    order_id=1001

    while True:
        yield order_id
        order_id+=1

orders=order_id_generator()

print(next(orders))
print(next(orders))
print(next(orders))
print(next(orders))
print(next(orders))
