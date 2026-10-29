from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool



item_1 = Product(name="bread", price=7.5, in_stock=True)
item_2 = Product(name="cheese", price=15, in_stock=True)
item_3 = Product(name="wine", price=1000000, in_stock=False)


print(item_1)
print(item_2)
print(item_3)
