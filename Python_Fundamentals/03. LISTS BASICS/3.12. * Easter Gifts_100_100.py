gifts_list = [x for x in input().split()]

while True:
    cmd = input()
    if cmd == 'No Money':
        break
    command = cmd.split()[0]
    if command == "OutOfStock":
        gift_0 = cmd.split()[1]
        for gift in gifts_list:
            if gift == gift_0:
                ind = gifts_list.index(gift)
                gifts_list[ind] = 'None'

    elif command == "Required":
        gift_1 = cmd.split()[1]
        ind_1 = int(cmd.split()[2])
        if 0 < ind_1 <= len(gifts_list) - 1:
            gifts_list[ind_1] = gift_1

    elif command == "JustInCase":
        gift_2 = cmd.split()[1]
        gifts_list[-1] = gift_2

final_list = [x for x in gifts_list if not x == "None"]
print(' '.join(final_list))
