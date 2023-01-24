def grades(value):
    if 2.00 <= value <= 2.99:
        print("Fail")
    elif 3.00 <= value <= 3.49:
        print("Poor")
    elif 3.50 <= value <= 4.49:
        print("Good")
    elif 4.50 <= value <= 5.49:
        print("Very Good")
    elif 5.50 <= value <= 6.00:
        print("Excellent")


def main():
    grade_value = float(input())
    grades(grade_value)


if __name__ == "__main__":
    main()
