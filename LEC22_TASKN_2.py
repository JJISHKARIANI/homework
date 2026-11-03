import requests 
import time
import threading


BASE_URL = 'https://jsonplaceholder.typicode.com/posts'


def fech_post(post_id):
    try:
        response = requests.get(f"{BASE_URL}/{post_id}")
        print(f'Post {post_id}')
        print(f"Status: {response.status_code}")
    except Exception as e:
        print(e) 

if __name__ == '__main__':
    threads = []

    start_time = time.time()

    for i in range(1, 101):
        thread = threading.Thread(target=fech_post, args=(i,))
        threads.append(thread)
        
    for t in threads:
        t.start()

    for t in threads:
        t.join()       

end_time = time.time()
total = end_time - start_time

print(f'total time taken is : {total:.4f} seconds')
