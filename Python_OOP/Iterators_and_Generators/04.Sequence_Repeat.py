class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.num = number
        self.idx = 0
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter <= self.num:
            self.counter += 1
            current = self.sequence[self.idx]
            self.idx += 1
            if self.idx > len(self.sequence) - 1:
                self.idx = 0
            return current
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
