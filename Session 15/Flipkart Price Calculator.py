def price_per_item():
    try:
        total_amount=float(input("Enter total cart amount: Rs."))
        item_count=int(input("Enter number of items: "))

        price=total_amount/item_count

        print(f"Price per item: Rs.{price:.2f}")

    except ZeroDivisionError:
        print("Sorry!!! The number of items cannot be zero.")
    except ValueError:
        print("Please enter valid numbers !!!")


price_per_item()
