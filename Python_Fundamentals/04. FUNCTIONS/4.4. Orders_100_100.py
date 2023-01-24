def calculate(num_1, num_2):
    result = num_1 * num_2
    return result


def main():
    product_name = input()
    product_quantity = int(input())
    products_dict = {"coffee": 1.50, "water": 1.00, "coke": 1.40, "snacks": 2.00}
    price = products_dict[product_name]
    print(f"{calculate(price, product_quantity):.2f}")


if __name__ == "__main__":
    main()
