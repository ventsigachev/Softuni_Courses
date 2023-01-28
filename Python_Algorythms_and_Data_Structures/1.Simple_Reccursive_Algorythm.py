# def iterative_factorial(n):
#     fact = 1
#     for i in range(2, n + 1):
#         fact *= i
#     return fact
#
#
# print(iterative_factorial(5))


# def recur_factorial(x):
#     if x == 1:
#         return x
#     else:
#         temp = recur_factorial(x - 1)
#         temp = temp * x
#     return temp


# print(recur_factorial(5))


# def recursive_factorial(y):
#     if y == 1: return y
#     else: return y * recursive_factorial(y - 1)
#
#
# print(recursive_factorial(5))


def r_factorial(z):
    return z if z == 1 else z * r_factorial(z - 1)


print(r_factorial(5))
