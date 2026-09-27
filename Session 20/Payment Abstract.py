from abc import ABC,abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self,amount):
        pass

class Paytm(PaymentMethod):
    
    def pay(self,amount):
        print(f"Paytm : Payment of Rs.{amount} Recieved Successfully !!!")

class PhonePe(PaymentMethod):

    def pay(self,amount):
        print(f"PhonePe : Payment of Rs.{amount} Recieved Successfully !!!")

paytm=Paytm()
phonepe=PhonePe()
paytm.pay(500)
phonepe.pay(1000)
