e_set = set()
o_set = set()

for ind in range(1, int(input()) + 1):
    string_name = input()
    sum_num = sum([ord(x) for x in string_name]) // ind

    if sum_num % 2 == 0:
        e_set.add(sum_num)
    else: o_set.add(sum_num)

e_set_sum = sum(e_set)
o_set_sum = sum(o_set)

if e_set_sum == o_set_sum:
    union = e_set | o_set
    print(", ".join(list(map(str, union))))
elif e_set_sum < o_set_sum:
    diff = o_set - e_set
    print(", ".join(list(map(str, diff))))
else:
    sym_diff = o_set ^ e_set
    print(", ".join(list(map(str, sym_diff))))
