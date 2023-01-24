def possible_permutations(numbers: list):
    final_list = []

    if len(numbers) == 0:
        final_list = final_list

    if len(numbers) == 1:
        final_list = [numbers]

    for i in range(len(numbers)):
        m = numbers[i]
        remnant_list = numbers[:i] + numbers[i + 1:]
        for p in possible_permutations(remnant_list):
            final_list.append([m] + p)

    for per in final_list:
        yield per


[print(n) for n in possible_permutations([1, 2, 3])]
