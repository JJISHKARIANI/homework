class Payment:
    def process_payment(self,amount):
        self.amount = amount
        print("Proceessing payment")



class CreditCardPayment(Payment):
    def __init__(self,amount):
        self.amount = amount

    def process_payment(self):    
        print(f"with credit card you paid {self.amount} GEL")


class PayPalPayment(Payment):
    def __init__(self,amount):
        self.amount = amount
    def process_payment(self):
        print(f"With PayPal card you paid {self.amount} GEL")    



result = Payment()
result.process_payment(300)

card_pay = CreditCardPayment(100)
card_pay.process_payment()
paypal_pay = PayPalPayment(200)
paypal_pay.process_payment()
    