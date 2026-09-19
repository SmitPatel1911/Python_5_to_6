def delivery_charge(amount,city):
    if city=="Ahmedabad":
        return 0
    else:
        return 50

print(delivery_charge(500,"Ahmedabad"))
print(delivery_charge(500,"Mumbai"))
