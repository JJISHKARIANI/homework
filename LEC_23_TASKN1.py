import asyncio
import requests
import time
import aiohttp






def fetch():
   
   start_time = time.time()

   for i in range(1, 11):
       URL = f'https://jsonplaceholder.typicode.com/posts/{i}'
       response = requests.get(URL)

   end_time = time.time()
   total = end_time - start_time
   return total



total_time = fetch()
print(total_time)





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
    start_time = time.time()
    URL = 'https://jsonplaceholder.typicode.com/posts/{}'
    
    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(*[fetch_data(session, URL.format(i) ) for i in range(1, 11)])        

        for response in responses:
            print(response)

    end_time = time.time()
    execution_time = end_time - start_time
    return  f'async func {total_time - execution_time} is seconds faster'        
    
if __name__ == '__main__':
    print(asyncio.run(main()))           

    