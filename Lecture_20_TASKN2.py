from dataclasses import  dataclass, asdict
import json


@dataclass
class Product:
    name: str
    price: float
    in_stock: bool


item_1 = Product(name="bread", price=7.5, in_stock=True)

python_data = asdict(item_1)

json_data = json.dumps(python_data, indent=4, sort_keys=True, ensure_ascii=False)
print(json_data)