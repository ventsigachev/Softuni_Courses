a_l, b_l = [int(x) for x in input().split()]
set_a = {input() for _ in range(a_l)}
set_b = {input() for _ in range(b_l)}
set_c = set_a & set_b
[print(x) for x in set_c]
