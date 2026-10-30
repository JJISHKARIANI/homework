import requests
from requests.exceptions import HTTPError,  ConnectTimeout
BASE_URL = 'https://crudcrud.com/api/a22d738c6e9748b58de514683f5bb8a3'
updated_product_data = {"name": "Gaming Laptop", "price": 3200, "in_stock": True}
product_id = '6ae4ff305b0e9703e8b9396f'


try:
    response = requests.delete(f"{BASE_URL}/product_data/{product_id}")
    response.raise_for_status()
    print("product deleted")

except HTTPError as e:
    print(e)

except ConnectTimeout as e:
    print(e)        