from functools import wraps


def logged(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        return f"you called {func.__name__}{args}\nit returned {result}"

    return wrapper


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
