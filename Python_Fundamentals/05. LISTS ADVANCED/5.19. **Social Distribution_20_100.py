initial_list = [int(num) for num in input().split(", ")]
minimum_wealth = int(input())

working_list = sorted(initial_list, reverse=True)
is_distribution = False
temp = 0

for i in range(len(working_list)):
    for j in range(i + 1, len(working_list)):
        if working_list[j] < minimum_wealth:
            temp = minimum_wealth - working_list[j]
            if working_list[i] - temp >= minimum_wealth:
                working_list[i] -= temp
                working_list[j] += temp
                is_distribution = True

social_distribution_list = list(reversed(working_list))

if is_distribution:
    print(social_distribution_list)
else:
    print("No equal distribution possible")
