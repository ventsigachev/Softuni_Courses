# (x − a)2 + (y − b)2 = r2 where a and b are the coordinates of the center (a, b) and r is the radius.
import math


def closest_point(list_):

    r_0 = math.sqrt(abs((list_[0][0] ** 2) + (list_[0][1] ** 2)))
    r_1 = math.sqrt(abs((list_[1][0] ** 2) + (list_[1][0] ** 2)))

    if r_0 <= r_1:
        print(f'{tuple(int(t) for t in list_[0])}{tuple(int(t) for t in list_[1])}')
    else:
        print(f'{tuple(int(t) for t in list_[1])}{tuple(int(t) for t in list_[0])}')


def longer_line(list_):
    line_nested_list = [list_[i:i + 2] for i in range(0, len(list_), 2)]
    line_1_list = line_nested_list[:2]
    line_2_list = line_nested_list[2:]

    line_1 = math.sqrt(abs(((line_1_list[0][0] - line_1_list[1][0]) ** 2) +
                           ((line_1_list[0][1] - line_1_list[1][1]) ** 2)))

    line_2 = math.sqrt(abs(((line_2_list[0][0] - line_2_list[1][0]) ** 2) +
                           ((line_2_list[0][1] - line_2_list[1][1]) ** 2)))

    if line_1 >= line_2:
        return closest_point(line_1_list)
    else:
        return closest_point(line_2_list)


def main():
    initial_list = list()

    for _ in range(8):
        initial_list.append(float(input()))

    longer_line(initial_list)


if __name__ == "__main__":
    main()
