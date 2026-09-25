class NoOffers(Exception):
    pass


def cashback_calculator():
    try:
        total_spend=float(input("Enter total spend: Rs."))
        offers=int(input("Enter number of offers applied: "))

        if offers==0:
            raise NoOffers("No offers were applied. Cannot calculate cashback.")

        average_cashback=total_spend/offers

        print(f"Average cashback per offer: Rs.{average_cashback:.2f}")

    except NoOffers as e:
        print("Error:",e)


cashback_calculator()
