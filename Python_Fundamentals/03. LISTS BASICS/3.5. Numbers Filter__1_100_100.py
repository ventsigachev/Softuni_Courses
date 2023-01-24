def even(list_):
    f_list = [x for x in list_ if not x % 2]
    print(f_list)


def odd(list_):
    f_list = [x for x in list_ if x % 2]
    print(f_list)


def positive(list_):
    f_list = list(filter(lambda x: x >= 0, list_))
    print(f_list)


def negative(list_):
    f_list = [x for x in list_ if x < 0]
    print(f_list)


def main():
    n = int(input())
    original_list = []
    for l in range(n):
        num = int(input())
        original_list.append(num)
    command = input()
    func = eval(command)
    func(original_list)


if __name__ == "__main__":
    main()
