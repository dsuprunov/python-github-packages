import time
from functools import wraps


def timing(func):
    """
    a timing decorator function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        finish = time.perf_counter()
        runtime = f"'{func.__name__}' took {(finish - start):.5f} second(s)"
        print(runtime)

        return result

    return wrapper
