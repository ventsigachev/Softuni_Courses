number_of_lines = int(input())
tank_capacity = 255
capacity = 0

for i in range(number_of_lines):
    volume = int(input())
    if volume <= tank_capacity:
        temporary = tank_capacity - volume
        tank_capacity = temporary
        capacity += volume
    else:
        print("Insufficient capacity!")
        continue
print(f"{capacity}")
