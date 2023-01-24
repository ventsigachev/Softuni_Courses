dict_heroes = {x: {} for x in input().split(", ")}

while True:
    t = input().split("-")
    if t[0] == "End":
        break
    n, i, c = t[0], t[1], int(t[2])
    if n in dict_heroes:
        if i not in dict_heroes[n]:
            dict_heroes[n][i] = c

final_list_heroes = [[k, len(v), sum([b for a, b in v.items()])] for k, v in dict_heroes.items()]
[print(f"{item[0]} -> Items: {item[1]}, Cost: {item[2]}") for item in final_list_heroes]
