import math


def closest_point(list_):
    tuples_list = [tuple(t) for t in [list_[i:i + 2] for i in range(0, len(list_), 2)]]

    r_0 = math.sqrt(abs((tuples_list[0][0] ** 2) + (tuples_list[0][1] ** 2)))
    r_1 = math.sqrt(abs((tuples_list[1][0] ** 2) + (tuples_list[1][0] ** 2)))

    if r_0 <= r_1:
        return tuples_list[0]
    else:
        return tuples_list[1]


def main():
    initial_list = list()

    for _ in range(4):
        initial_list.append(float(input()))

    print(closest_point(initial_list))


if __name__ == "__main__":
    main()
