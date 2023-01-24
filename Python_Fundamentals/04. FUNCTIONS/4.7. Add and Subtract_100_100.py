def add_and_subtract(a, b, c):

    def add(l, m):
        result_a = l + m
        return result_a

    def subtract(x, y):
        result_s = x - y
        return result_s

    result = subtract(add(a, b), c)
    return result


def main():
    print(add_and_subtract(int(input()), int(input()), int(input())))


if __name__ == "__main__":
    main()
