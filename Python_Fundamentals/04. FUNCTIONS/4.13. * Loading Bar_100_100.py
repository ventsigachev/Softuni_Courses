def loading_bar(num):

    validator = num // 10
    string_list = list(range(10))
    result = ''

    if validator < 10:
        for a in range(validator):
            string_list[a] = "%"
        for b in range(validator, 10):
            string_list[b] = "."

        result += f"{num}% [{''.join(string_list)}]\nStill loading..."

    elif validator == 10:
        result += "100% Complete!\n[%%%%%%%%%%]"

    return result


def main():
    print(loading_bar(int(input())))


if __name__ == "__main__":
    main()
