import math


def closest_point(list_):
    nested_list = [list_[i:i + 2] for i in range(0, len(list_), 2)]

    r_0 = math.sqrt(abs((nested_list[0][0] ** 2) + (nested_list[0][1] ** 2)))
    r_1 = math.sqrt(abs((nested_list[1][0] ** 2) + (nested_list[1][0] ** 2)))

    if r_0 <= r_1:
        return tuple(int(t) for t in nested_list[0])
    else:
        return tuple(int(t) for t in nested_list[1])


def main():
    initial_list = list()

    for _ in range(4):
        initial_list.append(float(input()))

    print(closest_point(initial_list))


if __name__ == "__main__":
    main()
