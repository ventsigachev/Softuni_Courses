initial_list = [int(num) for num in input().split()]
selector = int(input())

final_list = list()
i = 0

while initial_list:
    i = (i + selector - 1) % len(initial_list)
    final_list.append(initial_list.pop(i))

result_string = ",".join(map(str, final_list))
print(f'[{result_string}]')
