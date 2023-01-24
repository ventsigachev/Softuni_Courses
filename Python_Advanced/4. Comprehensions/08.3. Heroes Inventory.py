dicts_in_dict_heroes = {x: {} for x in input().split(", ")}

while True:
    t = input().split("-")
    if t[0] == "End":
        break
    n, i, c = t[0], t[1], int(t[2])
    if i not in dicts_in_dict_heroes[n]:
        dicts_in_dict_heroes[n][i] = c

[print(f"{h} -> Items: {len(dicts_in_dict_heroes[h])}, Cost: {sum(dicts_in_dict_heroes[h].values())}")
 for h in dicts_in_dict_heroes]
