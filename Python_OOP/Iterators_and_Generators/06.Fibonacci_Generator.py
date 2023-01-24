def fibonacci():
    starting_num = 0
    current_num = starting_num + 1

    while 1:
        yield starting_num
        starting_num, current_num = current_num, starting_num + current_num


generator = fibonacci()
for i in range(5):
    print(next(generator))
