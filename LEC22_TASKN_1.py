
import time
import  multiprocessing



def facto(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res 

if __name__ == '__main__':
    number = 5_000  

    start_time = time.time()
    result = facto(number)
    end_time = time.time()
    total = end_time - start_time
    print(f'total: {total:.4f}')



start_time = time.time()

if __name__ == '__main__':
    processes = [multiprocessing.Process(target=facto)]







end_time = time.time()










