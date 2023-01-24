command, initial_list = input(), [int(x) for x in input().split()]
odd_list, even_list = [], []
[odd_list.append(y) if not y % 2 == 0 else even_list.append(y) for y in initial_list]

if command == "Odd":
    print(sum(odd_list) * len(initial_list))
else:
    print(sum(even_list) * len(initial_list))
