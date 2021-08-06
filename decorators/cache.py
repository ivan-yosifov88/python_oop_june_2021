from functools import wraps


def cache(func):
    @wraps(func)
    def wrapper(n):
        log_key = n
        if log_key not in wrapper.log:
            wrapper.log[log_key] = func(n)
        return wrapper.log[log_key]
    wrapper.log = {}
    return wrapper



@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(7)
print(fibonacci.log)
fibonacci(4)
print(fibonacci.log)
