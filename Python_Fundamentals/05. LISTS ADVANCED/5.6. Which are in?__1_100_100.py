s_list = [s for s in input().split(", ")]
w_list = [w for w in input().split(", ")]
result_list = list()
[result_list.append(s) for s in s_list for w in w_list if s in w and s not in result_list]

print(result_list)
