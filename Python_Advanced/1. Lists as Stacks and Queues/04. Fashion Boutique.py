stack_clothes = [int(x) for x in input().split()]
capacity = int(input())
racks = 1
temp_capacity = 0

while stack_clothes:
    current = stack_clothes.pop()
    if temp_capacity + current <= capacity:
        temp_capacity += current
    else:
        stack_clothes.append(current)
        racks += 1
        temp_capacity = 0

print(racks)
