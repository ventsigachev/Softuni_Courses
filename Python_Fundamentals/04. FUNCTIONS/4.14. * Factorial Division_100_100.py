def factorial_division(num_1, num_2):

    def factorial(num):
        fact = 1

        for i in range(1, num + 1):
            fact = fact * i

        return fact

    fact_division = factorial(num_1) / factorial(num_2)
    result = f"{fact_division:.2f}"

    return result


def main():
    number_1 = int(input())
    number_2 = int(input())

    if number_1 > 0 and number_2 > 0:
        print(factorial_division(number_1, number_2))


if __name__ == "__main__":
    main()
