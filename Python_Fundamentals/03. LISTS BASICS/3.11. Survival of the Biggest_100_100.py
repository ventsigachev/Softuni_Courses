list_of_integers = [int(num) for num in input().split()]
n = int(input())

for i in range(n):
    min_num = min(list_of_integers)
    list_of_integers.remove(min_num)

print(list_of_integers)
