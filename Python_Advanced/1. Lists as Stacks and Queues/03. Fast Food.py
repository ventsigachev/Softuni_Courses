from collections import deque

all_food = int(input())
d_orders = deque([int(x) for x in input().split()])
is_valid = True

print(max(d_orders))

while d_orders:
    current = d_orders.popleft()
    if all_food >= current:
        all_food -= current
    else:
        is_valid = False
        d_orders.appendleft(current)
        break

if is_valid:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(str(x) for x in d_orders)}")
