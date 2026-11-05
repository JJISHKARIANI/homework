import asyncio
import requests
import aiohttp


URL = 'https://jsonplaceholder.typicode.com/posts/{id}'


async def fetch_data(session, url):
    try:
            timeout = aiohttp.ClientTimeout(total=10)
            async with session.get(url, timeout=timeout) as response:
                response.raise_for_status( )
                return await response.json() 
    
    except aiohttp.ClientResponseError as e:
            print(e)
    
    except aiohttp.ClientConnectionError as e:
            print('could not connect to the sever') 
    
    except aiohttp.ContentTypeError as e:
            print('invalid content type/json')
    
    except asyncio.TimeoutError as e:
            print('timeout')
    
    except Exception as e:
            print(e)               
    
async def main():
    URL = 'https://jsonplaceholder.typicode.com/posts/{}'
  
    
    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(*[fetch_data(session, URL.format(i) ) for i in range(1, 21)])
        for response in responses:
            if response.get("userId") == 1:
             print(response.get("title"))     


if __name__ == '__main__':
    print(asyncio.run(main()))  