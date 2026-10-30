import requests
from requests.exceptions import HTTPError, ConnectTimeout
BASE_URL = 'https://crudcrud.com/api/a22d738c6e9748b58de514683f5bb8a3'
id = '6ae506bad7b91f03e8dd87e1'


try:
    response = requests.get(f"{BASE_URL}/product_data/{id}", timeout=10)
    print(response.json())
    response.raise_for_status()

except HTTPError as e:
    print(e)    


except ConnectTimeout as e:
    print("Server took too long")

       