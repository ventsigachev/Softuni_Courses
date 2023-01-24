electrons = int(input())
electrons_list = []
idx = 1

while electrons > 0:
    electrons_on_level = 2 * idx ** 2
    if electrons >= electrons_on_level:
        electrons_list.insert(idx - 1, electrons_on_level)
    else:
        electrons_list.insert(idx - 1, electrons)
    electrons -= electrons_on_level
    idx += 1

print(electrons_list)
