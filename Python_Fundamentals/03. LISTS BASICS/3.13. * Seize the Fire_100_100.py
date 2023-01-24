input_list = [ch for ch in input().split("#")]
water = int(input())

cells_list = list()
effort = 0
cells_final_list = list()


for el in input_list:
    el_list = el.split(" = ")
    type_of_fire = el_list[0]
    range_of_fire = int(el_list[1])
    if type_of_fire == 'High':
        if 81 <= range_of_fire <= 125:
            cells_list.append(range_of_fire)
    elif type_of_fire == 'Medium':
        if 51 <= range_of_fire <= 80:
            cells_list.append(range_of_fire)
    elif type_of_fire == 'Low':
        if 1 <= range_of_fire <= 50:
            cells_list.append(range_of_fire)

for f in cells_list:
    if int(f) <= water:
        effort += f * 25 / 100
        cells_final_list.append(f)
        water -= f

total_fire = sum(cells_final_list)

print("Cells:")
for c in cells_final_list:
    print(f" - {c}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
