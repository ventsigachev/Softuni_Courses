def perfect_number(a):

    sum_ = 0
    result = ''

    for b in range(1, a):
        if a % b == 0:
            sum_ += b
    if sum_ == a:
        result += "We have a perfect number!"
    else:
        result += "It's not so perfect."

    return result


def main():
    print(perfect_number(int(input())))


if __name__ == "__main__":
    main()
