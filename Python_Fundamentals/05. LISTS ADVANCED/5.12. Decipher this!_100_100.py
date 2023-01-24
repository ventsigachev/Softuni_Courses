initial_list = [string for string in input().split()]
final_list = []

for el in initial_list:
    string_num = ''
    string_list = list()
    int_num = ''
    for a in el:
        if a.isnumeric():
            int_num += a
        else:
            string_list.append(a)
    alpha_num = chr(int(int_num))
    string_list.insert(0, alpha_num)
    string_list[-1], string_list[1] = string_list[1], string_list[-1]
    final_list.append(string_list)

for l in final_list:
    print(''.join(l), end=' ')
