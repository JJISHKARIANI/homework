import requests
from requests.exceptions import HTTPError,  ConnectTimeout
BASE_URL = 'https://crudcrud.com/api/a22d738c6e9748b58de514683f5bb8a3'
product_data = {
    "name": "Laptop", 
    "price": 2500, 
    "in_stock": True
}

try:
    response = requests.get(f"{BASE_URL}/product_data", timeout=10)
    data = response.json()
    response.raise_for_status()

except HTTPError as e:
    print(e)


except ConnectTimeout as e:
    print("Server took too long")

for i in data:
    print (f'id: {i["_id"]} name: {i["name"]}, price: {i['price']}, in_stock: {i["in_stock"]}')