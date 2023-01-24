def the_smallest(list_):
    result = min(list_)
    return result


def main():
    list_num = list()
    for _ in range(3):
        num = int(input())
        list_num.append(num)

    print(the_smallest(list_num))


if __name__ == "__main__":
    main()
