from time import time
from functools import wraps

def timing(func, *args):
    print("Timing func", func, "withs args:", args)
    start_time = time()
    print("Start time:", start_time)
    res = func(*args)
    end_time = time()
    print("End time:", end_time)
    work_time = end_time - start_time
    print("Work time:", work_time)
    print("Result:", res)
    return res

def decorator(func):
    @wraps(func)
    def wrapper(*args):
        return timing(func, *args)
    return wrapper

@decorator
def div(a, b, c):
    return (a // b // c)

@decorator
def pow(a, b):
    return a ** b

pow(10_000_000, 10_000)