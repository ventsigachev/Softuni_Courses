initial_list = [int(num) for num in input().split(", ")]
minimum_wealth = int(input())


is_distribution = False
temp = 0
max_num_idx = 0

for i in range(len(initial_list)):
    idx = i + 1
    if idx <= len(initial_list) - 1:
        if initial_list[i] < initial_list[idx]:
            max_num_idx = idx
for j in range(len(initial_list)):
    if initial_list[j] < minimum_wealth:
        temp = minimum_wealth - initial_list[j]
        if initial_list[max_num_idx] - temp >= minimum_wealth:
            initial_list[max_num_idx] -= temp
            initial_list[j] += temp
            is_distribution = True

if is_distribution:
    print(initial_list)
else:
    print("No equal distribution possible")
