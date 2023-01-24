input_list = input().split()
bakery_dict = dict()

for i in range(0, len(input_list), 2):
    key = input_list[i]
    value = input_list[i + 1]
    bakery_dict[key] = int(value)

print(bakery_dict)
