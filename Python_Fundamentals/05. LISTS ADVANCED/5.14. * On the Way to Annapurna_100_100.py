stores_items = dict()
result = ""

while True:
    data = input().split("->")
    if data[0] == "END":
        break
    elif data[0] == "Add":
        list_items = data[2].split(",")
        if data[1] not in stores_items:
            stores_items[data[1]] = []
            stores_items[data[1]].extend(list_items)
        else:
            stores_items[data[1]].extend(list_items)
    elif data[0] == "Remove":
        if data[1] in stores_items.keys():
            del stores_items[data[1]]

sorted_stores = sorted(sorted(stores_items.keys(), key=lambda x: [x], reverse=True), key=lambda x: -len(stores_items[x]))
result += f"Stores list:\n"
for store in sorted_stores:
    result += f"{store}\n"
    for item in stores_items[store]:
        result += f"<<{item}>>\n"

print(result)
