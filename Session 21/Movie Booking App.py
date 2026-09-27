class Ticket:
    def __init__(self,movie_name,price):
        self.movie_name=movie_name
        self.price=price

    def get_final_price(self):
        return self.price


class PremiumTicket(Ticket):
    def get_final_price(self):
        return super().get_final_price()+50

normal_ticket=Ticket("Inception",200)
premium_ticket=PremiumTicket("Inception",200)
print("Movie : ",normal_ticket.movie_name)
print("Normal Ticket Price : Rs.", normal_ticket.get_final_price())
print("* "*30)
print("Movie:", premium_ticket.movie_name)
print("Premium Ticket Price : Rs.", premium_ticket.get_final_price())
