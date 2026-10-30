import requests
from requests.exceptions import HTTPError,  ConnectTimeout
BASE_URL = 'https://crudcrud.com/api/a22d738c6e9748b58de514683f5bb8a3'
updated_product_data = {"name": "Gaming Laptop", "price": 3200, "in_stock": True}
product_id =  '6ae50612d7b91f03e8dd87e0'

try:
    response = requests.put(f'{BASE_URL}/product_data/{product_id}', json=updated_product_data , timeout=10)
    
    print(response.status_code)
    response.raise_for_status()

except HTTPError as e:
    print(e)

except ConnectTimeout as e:
    print("Server took too long")