parking_dict = dict()
n = int(input())
result = ''

for _ in range(n):
    data = input().split()
    if data[0] == 'register':
        name, plate = data[1], data[2]
        if name not in parking_dict:
            parking_dict[name] = plate
            result += f"{name} registered {plate} successfully\n"
        else:
            if parking_dict[name] == plate:
                result += f"ERROR: already registered with plate number {plate}\n"
    elif data[0] == 'unregister':
        name = data[1]
        if name in parking_dict:
            del parking_dict[name]
            result += f"{name} unregistered successfully\n"
        else:
            result += f"ERROR: user {name} not found\n"

for k, v in parking_dict.items():
    result += f"{k} => {v}\n"

print(result)
