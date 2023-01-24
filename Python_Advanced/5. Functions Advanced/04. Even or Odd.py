def even_odd(*args):
    command = args[-1]
    final_list = []
    if command == "even":
        [final_list.append(y) for y in args[:-1] if y % 2 == 0]
    else:
        [final_list.append(y) for y in args[:-1] if not y % 2 == 0]
    return final_list


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
