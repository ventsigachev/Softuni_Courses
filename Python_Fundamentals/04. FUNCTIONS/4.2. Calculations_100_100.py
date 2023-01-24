def multiply(a, b):
    print(a * b)


def divide(a, b):
    print(a // b)


def add(a, b):
    print(a + b)


def subtract(a, b):
    print(a - b)


def main():
    func = input()
    f_n = int(input())
    s_n = int(input())
    func_dict = {"multiply": multiply, "divide": divide, "add": add, "subtract": subtract}
    func_dict[func](f_n, s_n)


if __name__ == "__main__":
    main()
