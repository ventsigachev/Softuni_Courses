roads_dict = dict()
result = ''

while True:
    data = input().split("->")
    if data[0] == "END":
        break
    elif data[0] == "Add":
        if not data[1] in roads_dict.keys():
            roads_dict[data[1]] = []
            roads_dict[data[1]].append(data[2])
        else:
            roads_dict[data[1]].append(data[2])
    elif data[0] == "Move":
        if data[2] in roads_dict[data[1]]:
            roads_dict[data[3]].append(data[2])
            roads_dict[data[1]].remove(data[2])
    elif data[0] == "Close":
        del roads_dict[data[1]]

sorted_roads = sorted(roads_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
result += f"Practice sessions:\n"

for t in sorted_roads:
    result += f"{t[0]}\n"
    for racer in t[1]:
        result += f"++{racer}\n"

print(result)
