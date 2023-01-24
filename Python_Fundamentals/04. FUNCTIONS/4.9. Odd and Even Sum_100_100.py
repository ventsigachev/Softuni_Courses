def odd_even_sum(string_):
    odd_list = list()
    even_list = list()

    for el in string_:
        if int(el) % 2 == 0:
            even_list.append(int(el))
        else:
            odd_list.append(int(el))

    result = f"Odd sum = {sum(odd_list)}, Even sum = {sum(even_list)}"
    return result


def main():
    print(odd_even_sum(input()))


if __name__ == "__main__":
    main()
