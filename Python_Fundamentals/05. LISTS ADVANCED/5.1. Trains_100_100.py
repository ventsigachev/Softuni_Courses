train_list = list()
num = int(input())

for _ in range(num):
    train_list.append(0)

while True:
    command = input().split()
    if command[0] == 'End':
        break
    elif command[0] == 'add':
        people = int(command[1])
        train_list[-1] += people
    elif command[0] == 'insert':
        idx_i = int(command[1])
        people_i = int(command[2])
        train_list[idx_i] += people_i
    elif command[0] == 'leave':
        idx_l = int(command[1])
        people_l = int(command[2])
        train_list[idx_l] -= people_l

print(train_list)
