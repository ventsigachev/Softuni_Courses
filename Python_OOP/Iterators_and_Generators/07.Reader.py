def read_next(*args):
    for arg in args:
        for e in arg:
            yield str(e)


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
