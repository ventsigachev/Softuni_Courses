dicts_in_list_heroes = [{"Name": x, "Items": [], "Cost": 0, } for x in input().split(", ")]

while True:
    t = input().split("-")
    if t[0] == "End":
        break
    n, i, c = t[0], t[1], int(t[2])
    for y in dicts_in_list_heroes:
        if n == y["Name"] and i not in y["Items"]:
            y["Items"].append(i)
            y["Cost"] += c

[print(f"{h['Name']} -> Items: {len(h['Items'])}, Cost: {h['Cost']}") for h in dicts_in_list_heroes]
