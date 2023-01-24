list_ = [int(num) for num in input().split()]
middle = len(list_) // 2
list_left = list_[: middle]
list_right = list_[middle + 1:][::-1]
time_left = 0
time_right = 0

for num in list_left:
    if not num == 0:
        time_left += num
    else:
        time_left = time_left * 0.8

for num in list_right:
    if not num == 0:
        time_right += num
    else:
        time_right = time_right * 0.8

if time_left < time_right:
    print(f"The winner is left with total time: {time_left:.1f}")
else:
    print(f"The winner is right with total time: {time_right:.1f}")
