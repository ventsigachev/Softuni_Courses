import math


def closer_point(a1, b1, a2, b2):
    first_point = math.sqrt((a1 ** 2) + (b1 ** 2))
    second_point = math.sqrt((a2 ** 2) + (b2 ** 2))

    if first_point <= second_point:
        print(f"({int(a1)}, {int(b1)})({int(a2)}, {int(b2)})")
    else:
        print(f"({int(a2)}, {int(b2)})({int(a1)}, {int(b1)})")


def longer_line(list_):

    line_1_l = math.sqrt(math.pow((list_[2] - list_[0]), 2) + math.pow((list_[3] - list_[1]), 2))
    line_2_l = math.sqrt(math.pow((list_[6] - list_[4]), 2) + math.pow((list_[7] - list_[5]), 2))

    if line_1_l >= line_2_l:
        closer_point(list_[0], list_[1], list_[2], list_[3])
    else:
        closer_point(list_[4], list_[5], list_[6], list_[7])


def main():
    list_points = []
    for _ in range(8):
        list_points.append(float(input()))

    longer_line(list_points)


if __name__ == "__main__":
    main()
