num_list = [int(x) for x in input().split(", ")]
num_beggars = int(input())
sum_list = list()
ind = 0

for beggar in range(1, num_beggars + 1):
    sum_beggar = 0
    for i in range(ind, len(num_list), num_beggars):
        sum_beggar += num_list[i]
    sum_list.append(sum_beggar)
    ind += 1

print(sum_list)
