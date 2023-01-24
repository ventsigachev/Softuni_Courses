number = input()
max_number = ''
list_num = list(number)

for i in range(0, len(list_num)):
    max_digit = max(list_num)
    max_number += str(max_digit)
    list_num.remove(max_digit)

print(max_number)
