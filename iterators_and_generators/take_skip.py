class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        current_number = self.start
        self.start += self.step
        self.count -= 1
        return current_number



numbers = take_skip(2, 6)
for number in numbers:
    print(number)


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
# if self.count > 0:
        #     current_number = self.start
        #     self.start += self.step
        #     self.count -= 1
        #     return current_number
        # else:
        #     raise StopIteration