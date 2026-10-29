import json
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool




json_data = '{"name": "Laptop", "price": 2500, "in_stock": true}'


python_loads = json.loads(json_data)
p = Product(** python_loads)
print(p)
print(f"name: {p.name}, price: {p.price}, in_stock: {p.in_stock}")
