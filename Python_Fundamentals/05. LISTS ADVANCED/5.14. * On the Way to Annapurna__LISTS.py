stores_item = list()

while True:
    data = input().split("->")
    if data[0] == "END":
        break
    elif data[0] == "Add":
        while len(stores_item) > 0:
            for store in stores_item:
                if not store[0] == data[1]:
                    stores_item += [[data[1], data[2].split(",")]]
                    break
                else:
                    store[1].extend(data[2].split(","))
        else:
            stores_item += [[data[1], data[2].split(",")]]
    elif data[0] == "Remove":
        for store in stores_item:
            if store[0] == data[1]:
                del store

print(stores_item)
