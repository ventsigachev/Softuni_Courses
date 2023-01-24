initial_list = [int(num) for num in input().split(", ")]
boundary = 10
result = ''

while initial_list:
    list_boundary = []
    for idx in range(len(initial_list) - 1, -1, -1):
        if initial_list[idx] <= boundary:
            list_boundary.append(initial_list.pop(idx))
    list_boundary.reverse()
    print(f"Group of {boundary}\'s: {list_boundary}")
    boundary += 10
