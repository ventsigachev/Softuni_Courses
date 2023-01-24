def palindrome(list_):

    result_list = ["True" if list(el) == list(el)[::-1] else "False" for el in list_]

    for word in result_list:
        print(word)


def main():
    palindrome([num for num in input().split(", ")])


if __name__ == "__main__":
    main()
