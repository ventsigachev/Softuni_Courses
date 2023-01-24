final_list = list()
is_first_match = False
is_second_match = False

for _ in range(3):
    list_ = [int(x) for x in input().split()]
    final_list.extend(list_)

i = 0
step = 1
for _ in range(3):
    if final_list[i] == 1 and final_list[i + step] == 1 and final_list[i + 2 * step] == 1:
        is_first_match = True
    elif final_list[i] == 2 and final_list[i + step] == 2 and final_list[i + 2 * step] == 2:
        is_second_match = True
    if is_first_match or is_second_match:
        break
    i += 3

i = 0
step = 3
for _ in range(3):
    if final_list[i] == 1 and final_list[i + step] == 1 and final_list[i + 2 * step] == 1:
        is_first_match = True
    elif final_list[i] == 2 and final_list[i + step] == 2 and final_list[i + 2 * step] == 2:
        is_second_match = True
    if is_first_match or is_second_match:
        break
    i += 1

i = 0
step = 4
if final_list[i] == 1 and final_list[i + step] == 1 and final_list[i + 2 * step] == 1:
    is_first_match = True
elif final_list[i] == 2 and final_list[i + step] == 2 and final_list[i + 2 * step] == 2:
    is_second_match = True

if final_list[2] == 1 and final_list[4] == 1 and final_list[6] == 1:
    is_first_match = True
elif final_list[2] == 2 and final_list[4] == 2 and final_list[6] == 2:
    is_second_match = True

if is_first_match:
    print("First player won")
elif is_second_match:
    print("Second player won")
else:
    print("Draw!")
