class Payment:
    def process_payment(self,amount):
        self.amount = amount
        print("Proceessing payment")



class CreditCardPayment(Payment):
    def process_payment(self, amount):
        super().process_payment(amount)
        print(f"With Credit Card: Its paid {self.amount} GEL ")


class PayPalPayment(Payment):
    def process_payment(self, amount):
        super().process_payment(amount)        
        print(f"With Paypal: Its paid {self.amount} GEL")

    












result = Payment()


card_pay = CreditCardPayment()
card_pay.process_payment(100)
paypal_pay = PayPalPayment()
paypal_pay.process_payment(200)
    