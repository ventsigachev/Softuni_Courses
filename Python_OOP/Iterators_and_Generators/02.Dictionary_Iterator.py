class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.d = dictionary
        self.lst = list(dictionary)
        self.length = len(dictionary)
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < self.length:
            c_key = self.lst[self.idx]
            c_value = self.d[c_key]
            self.idx += 1
            return c_key, c_value
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
