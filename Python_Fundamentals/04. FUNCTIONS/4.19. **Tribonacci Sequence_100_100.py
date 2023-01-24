def tribonacci_count(num):
    num3 = 1
    num2 = 1
    num1 = 2
    max_num = num

    for _ in range(max_num - 3):
        num = num3 + num2 + num1
        num3 = num2
        num2 = num1
        num1 = num
        print(f"{num} ", end='')


def main():
    num_input = int(input())
    if num_input <= 0:
        print('0', end='')
    elif num_input == 1:
        print('1', end='')
    elif num_input == 2:
        print(f"1 1", end='')
    elif num_input == 3:
        print("1 1 2", end="")
    else:
        print(f"1 1 2 ", end='')
        tribonacci_count(num_input)


if __name__ == "__main__":
    main()
