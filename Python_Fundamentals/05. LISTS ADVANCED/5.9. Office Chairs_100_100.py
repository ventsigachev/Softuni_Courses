counter = int(input())
free_chairs = 0
needed_chairs = ''

for i in range(1, counter + 1):
    data = input().split()
    chairs_list = [str(x) for x in data[0]]
    people = int(data[1])
    if len(chairs_list) >= people:
        free_chairs += len(chairs_list) - people
    else:
        chairs = people - len(chairs_list)
        needed_chairs += f"{chairs} more chairs needed in room {i}\n"

if not needed_chairs:
    print(f"Game On, {free_chairs} free chairs left")
else:
    print(needed_chairs)
