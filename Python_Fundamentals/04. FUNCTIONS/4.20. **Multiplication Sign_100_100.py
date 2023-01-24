def positive(list_):

    counter_n = 0
    counter_p = 0

    for num in list_:
        if num < 0:
            counter_n += 1
        elif num > 0:
            counter_p += 1
    if (counter_n == 2 and counter_p == 1) or (counter_n == 0 and counter_p == 3):
        return "positive"


def negative(list_):

    counter = 0

    for num in list_:
        if num < 0:
            counter += 1
    if counter % 2 == 1:
        return "negative"


def zero(list_):

    counter = 0

    for num in list_:
        if num == 0:
            counter += 1
    if counter > 0:
        return "zero"


def decision(list_):
    dec_list = [zero(list_), negative(list_), positive(list_)]

    for el in dec_list:
        if el:
            return el


def main():
    initial_list = list()

    for _ in range(3):
        initial_list.append(int(input()))

    print(decision(initial_list))


if __name__ == "__main__":
    main()
