food_apps=["Zomato","Swiggy","Domino's","Uber Eats","EatSure"]

app_iterator=iter(food_apps)

try:
    while True:
        app = next(app_iterator)
        print(app)
except StopIteration:
    pass
