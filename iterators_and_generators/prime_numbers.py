from math import sqrt


def is_prime(number):
    if number < 2:
        return False
    for num in range(2, int(sqrt(number)) + 1):
        if number % num == 0:
            return False
    return True


def get_primes(ll):
    for number in ll:
        if is_prime(number):
            yield number

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))