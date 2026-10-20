class Product():
    shop_name = "MegaShop"


    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


    def sell(self, quantity):
        self.quantity = quantity
        self.stock -= quantity
        print(f"shop sold {quantity} {self.name} and now is remaining {self.stock}")


Laptop = Product("laptop", 1500, 10)
print('=' * 40)
Laptop.sell(2)

Book = Product("Book", 50, 100)
print('=' * 40)
Book.sell(20)

