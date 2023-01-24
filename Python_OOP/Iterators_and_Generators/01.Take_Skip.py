class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.counter = 1
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter <= self.count:
            current = self.start
            self.start += self.step
            self.counter += 1
            return current
        raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
