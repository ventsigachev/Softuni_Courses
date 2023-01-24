input_list = [chs for chs in input().split()]
sum_all = 0

for char in input_list:
    sum_t_list = [ch for ch in char if ch.isdigit()]
    sum_t_result = int("".join(sum_t_list))
    f_l = char[0]
    l_l = char[-1]
    if char[0].isupper():
        sum_t_result /= ord(f_l.lower()) - 96
    else:
        sum_t_result *= ord(f_l) - 96
    if char[-1].isupper():
        sum_t_result -= ord(l_l.lower()) - 96
    else:
        sum_t_result += ord(l_l) - 96
    sum_all += sum_t_result

print(f"{sum_all:.2f}")
