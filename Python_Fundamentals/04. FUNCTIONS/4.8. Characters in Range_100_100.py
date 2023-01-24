def characters_printing(a, b):
    first = ord(a)
    last = ord(b)
    list_characters = list()

    if first < last:
        first += 1
        while first < last:
            list_characters.append(chr(first))
            first += 1
    else:
        last += 1
        for char in range(last, first):
            list_characters.append(chr(char))

    return list_characters


def main():
    print(*characters_printing(input(), input()))


if __name__ == "__main__":
    main()
