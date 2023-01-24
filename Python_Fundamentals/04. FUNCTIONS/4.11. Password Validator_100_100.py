def password_validator(string_):

    is_valid = True

    if not 6 <= len(string_) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False

    if not string_.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False

    if len([x for x in string_ if x.isdigit()]) < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")


def main():
    password_validator(input())


if __name__ == "__main__":
    main()
