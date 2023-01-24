checker = [['x', 'x', 'x', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', 'x', 'x', 'x', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', 'x', 'x', 'x'], ['x', '_', '_', 'x', '_', '_', 'x', '_', '_'],
           ['_', 'x', '_', '_', 'x', '_', '_', 'x', '_'], ['_', '_', 'x', '_', '_', 'x', '_', '_', 'x'],
           ['x', '_', '_', '_', 'x', '_', '_', '_', 'x'], ['_', '_', 'x', '_', 'x', '_', 'x', '_', '_']]

final_list = list()
is_first_match = False
is_second_match = False

for r in range(3):
    list_ = [int(x) for x in input().split()]
    final_list.extend(list_)

i = 1
for _ in range(2):
    list_to_check = list()
    for num in final_list:
        if num == i:
            list_to_check.append("x")
        else:
            list_to_check.append("_")

    if list_to_check in checker and i == 1:
        is_first_match = True
    elif list_to_check in checker and i == 2:
        is_second_match = True
    else:
        i += 1
        continue

if is_first_match:
    print("First player won")
elif is_second_match:
    print("Second player won")
else:
    print("Draw!")
