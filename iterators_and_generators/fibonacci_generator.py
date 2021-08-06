def fibonacci():
    previous_number = 0
    next_number = 1
    while True:
        current_number = previous_number
        yield previous_number
        previous_number = next_number
        next_number = current_number + previous_number


generator = fibonacci()
for i in range(20):
    print(next(generator))
