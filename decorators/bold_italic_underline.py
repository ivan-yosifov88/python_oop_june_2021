from functools import wraps


def make_bold(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        return f"<b>{result}</b>"

    return wrapper


def make_italic(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        return f"<i>{result}</i>"

    return wrapper


def make_underline(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        return f"<u>{result}</u>"

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))
