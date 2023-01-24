orders_dict = dict()

while True:
    data = input().split()
    if data[0] == "buy":
        break
    name, pr, qua = data[0], float(data[1]), int(data[2])
    if name not in orders_dict:
        orders_dict[name] = [0.0, 0]
    orders_dict[name][0] = pr
    orders_dict[name][1] += qua

for k, vs in orders_dict.items():
    print(f"{k} -> {(vs[0] * vs[1]):.2f}")
