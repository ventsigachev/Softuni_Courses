sanctuary_animals = list()
animal_area = []
result = ""

while True:
    data = input().split(":")
    if data[0] == "Last Info":
        break
    elif data[0] == "Add":
        is_animals = False
        for animal in sanctuary_animals:
            if animal[0] == data[1]:
                is_animals = True
                animal[1] += int(data[2])
                break
            else:
                is_animals = False
        if not is_animals:
            sanctuary_animals += [[data[1], int(data[2]), data[3]]]

    elif data[0] == "Feed":
        for animal in sanctuary_animals:
            if animal[0] == data[1]:
                animal[1] -= int(data[2])
                if animal[1] <= 0:
                    sanctuary_animals.remove(animal)
                    result += f"{animal[0]} was successfully fed\n"

for animal_ in sanctuary_animals:
    is_animal_a = False
    for animal_a in animal_area:
        if animal_a[0] == animal_[2]:
            is_animal_a = True
            animal_a[1] += 1
            break
    if not is_animal_a:
        animal_area += [[animal_[2], 1]]

sorted_animals = sorted(sanctuary_animals, key=lambda x: (-x[1], x[0]))
sorted_areas = sorted(animal_area, key=lambda x: -x[1])

result += f"Animals:\n"
for an in sorted_animals:
    result += f"{an[0]} -> {an[1]}g\n"
result += f"Areas with hungry animals:\n"
for ar in sorted_areas:
    result += f"{ar[0]} : {ar[1]}\n"
print(result)
