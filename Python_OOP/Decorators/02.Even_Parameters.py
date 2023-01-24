def even_parameters(func):
    def wrapper(*args):
        is_legit = True
        for a in args:
            if not isinstance(a, int) or not a % 2 == 0:
                is_legit = False
        result = func(*args) if is_legit else "Please use only even numbers!"
        return result
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
