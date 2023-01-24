list_to_manipulate = [str(x) for x in input().split()]
repeater = int(input())

for _ in range(repeater):
    list_len = int(len(list_to_manipulate) / 2)
    list_first_half = list_to_manipulate[:list_len]
    list_second_half = list_to_manipulate[list_len:]
    list_to_manipulate = list()
    for i in range(list_len):
        list_to_manipulate.append(list_first_half[i])
        list_to_manipulate.append(list_second_half[i])

print(list_to_manipulate)
