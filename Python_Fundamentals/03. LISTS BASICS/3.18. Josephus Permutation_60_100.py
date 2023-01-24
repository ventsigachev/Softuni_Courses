def permutations(list_, num):
    permutations_list = list()
    num -= 1
    index = num
    while len(list_) >= 1:
        d = list_.pop(index)
        permutations_list.append(d)
        if len(list_) > 0:
            index = (index + num) % len(list_)
    string = "[" + ",".join(str(num) for num in permutations_list) + "]"
    print(string)


def main():
    initial_list = [int(num) for num in input().split()]
    number = int(input())
    permutations(initial_list, number)


if __name__ == "__main__":
    main()
