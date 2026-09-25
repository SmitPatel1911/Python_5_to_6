def safe_divide_for_zomato(bill_amount,number_of_people):
    try:
        result=bill_amount/number_of_people

    except ZeroDivisionError:
        print("Error!!!: Number of people cannot be zero.")

    else:
        print(f"Each person pays: Rs.{result:.2f}")

    finally:
        print("Split calculation done !!!")


safe_divide_for_zomato(1200,4)
print("* "*50)
safe_divide_for_zomato(1200,0)
