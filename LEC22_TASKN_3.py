from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import requests





BASE_URL = 'https://jsonplaceholder.typicode.com/posts'


def fech_post(post_id):
    try:
        response = requests.get(f"{BASE_URL}/{post_id}")
        print(f'Post {post_id}')
        print(f"Status: {response.status_code}")
    except Exception as e:
        print(e) 

if __name__ == '__main__':
    start_time = time.time()


    with ThreadPoolExecutor(max_workers=15) as executor:
        result = list(executor.map(fech_post, range(1, 101)))

    end_time = time.time()
    total_time = end_time - start_time

print(f'total time taken: {total_time:.4f} seconds')    




