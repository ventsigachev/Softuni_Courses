import sys

multiplied_list = list()
counter = 0
factor = int(input())
len_list = int(input())

for num in range(1, sys.maxsize - 1):
    if num % factor == 0:
        counter += 1
        multiplied_list.append(num)
    if counter == len_list:
        break

print(multiplied_list)
