animal_sanctuary = dict()
a_area_count = dict()
result = ''

while True:
    data = input().split(":")
    if data[0] == "Last Info":
        break
    elif data[0] == "Add":
        if data[1] not in animal_sanctuary:
            animal_sanctuary[data[1]] = {"a_food": int(data[2]), "a_area": data[3]}
        else:
            animal_sanctuary[data[1]]['a_food'] += int(data[2])
    elif data[0] == "Feed":
        if data[1] in animal_sanctuary:
            animal_sanctuary[data[1]]["a_food"] -= int(data[2])
            if animal_sanctuary[data[1]]["a_food"] <= 0:
                result += f"{data[1]} was successfully fed\n"
                del animal_sanctuary[data[1]]

sorted_a_food = sorted(animal_sanctuary.keys(), key=lambda x: (-animal_sanctuary[x]["a_food"], [x]))
result += "Animals:\n"
for animal in sorted_a_food:
    result += f"{animal} -> {animal_sanctuary[animal]['a_food']}g\n"

for name in animal_sanctuary.keys():
    area = animal_sanctuary[name]["a_area"]
    if area in a_area_count:
        a_area_count[area] += 1
    else:
        a_area_count[area] = 1

result += "Areas with hungry animals:\n"
for k in sorted(a_area_count.keys(), key=lambda x: -a_area_count[x]):
    result += f"{k} : {a_area_count[k]}\n"

print(result)
