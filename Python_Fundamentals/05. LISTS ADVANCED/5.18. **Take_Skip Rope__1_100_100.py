initial_list = [el for el in input()]
non_numbers_list = list()
numbers_list = list()
take_list = list()
skip_list = list()
result = []

[numbers_list.append(int(s)) if s.isnumeric() else non_numbers_list.append(s) for s in initial_list]
[take_list.append(numbers_list[i]) if not i % 2
 else skip_list.append(numbers_list[i]) for i in range(len(numbers_list))]

for i1, i2 in zip(take_list, skip_list):
    result += non_numbers_list[: i1]
    non_numbers_list = non_numbers_list[i1 + i2:]

print("".join(result))
