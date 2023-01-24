input_str = input()
result_str = ""
temp_str = ''
i = 0

while i <= len(input_str) - 1:
    while not input_str[i].isdigit():
        temp_str += input_str[i].upper()
        i += 1
    else:
        multiplier_str = ''
        while i <= len(input_str) - 1 and input_str[i].isdigit():
            multiplier_str += input_str[i]
            i += 1
        multiplier = int(multiplier_str)
        result_str += temp_str * multiplier
        temp_str = ''

print(f"Unique symbols used: {len(set(result_str))}")
print(f"{result_str}")
