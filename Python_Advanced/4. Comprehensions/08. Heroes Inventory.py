dict_heroes = {x: {} for x in input().split(", ")}

while True:
    t = input().split("-")
    if t[0] == "End":
        break
    n, i, c = t[0], t[1], int(t[2])
    if n in dict_heroes:
        if i not in dict_heroes[n]:
            dict_heroes[n][i] = c

for k, v in dict_heroes.items():
    print(f"{k} -> Items: {len(v)}, Cost: {sum([b for a, b in v.items()])}")
