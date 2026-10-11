import time 
from functools import wraps



def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"running {func.__name__} executed in {execution_time:.2f} seconds")
        return result
    return wrapper

@log_execution
def my_function():
    """this function is example"""
    time.sleep(1.5)
    return "done"

result = my_function()

print("name:", my_function.__name__)
print("Docstring:", my_function.__doc__)



