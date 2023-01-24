def data_manipulations(typo, string):

    if typo == "int":
        num = int(string)
        return num * 2

    elif typo == "real":
        num = float(string)
        return f'{(num * 1.5):.2f}'
    elif typo == "string":
        return f'${string}$'


def main():
    print(data_manipulations(input(), input()))


if __name__ == "__main__":
    main()
