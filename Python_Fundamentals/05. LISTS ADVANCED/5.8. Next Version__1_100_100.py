initial_list = [str(num) for num in input().split(".")]
initial_number = int(''.join(initial_list))
initial_number += 1
str_number = str(initial_number)
number = str_number.zfill(3)
number_list = [s for s in number]

print('.'.join(number_list))
