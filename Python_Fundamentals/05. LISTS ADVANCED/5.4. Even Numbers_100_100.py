initial_list = [int(x) for x in input().split(", ")]
indexes_list = [initial_list.index(num) for num in initial_list if not num % 2]
print(indexes_list)
