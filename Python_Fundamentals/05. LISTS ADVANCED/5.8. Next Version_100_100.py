initial_list = [str(num) for num in input().split(".")]
initial_number = int(''.join(initial_list))
number_list = []

initial_number += 1

if initial_number < 10:
    number = f"00{initial_number}"
    [number_list.append(num) for num in number]
elif 10 <= initial_number < 100:
    number = f"0{initial_number}"
    [number_list.append(num) for num in number]
elif 100 <= initial_number <= 999:
    number = f"{initial_number}"
    [number_list.append(num) for num in number]

print('.'.join(number_list))
