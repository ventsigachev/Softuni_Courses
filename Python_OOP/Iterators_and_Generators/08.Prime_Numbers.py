def get_primes(numbers: list):
    positive_list = [x for x in numbers if x > 1]

    for num in positive_list:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
