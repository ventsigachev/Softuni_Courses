initial_list = [0 for _ in range(10)]

while True:
    command = input().split("-")
    if command[0] == 'End':
        break
    else:
        idx = int(command[0])
        notes = command[1]
        initial_list.insert(idx, notes)

to_do_list = [el for el in initial_list if el]

print(to_do_list)
