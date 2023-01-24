statistic_dict = dict()

while True:
    data = input().split(": ")
    if data[0] == "statistics":
        break
    else:
        key, value = data[0], int(data[1])
        if key not in statistic_dict:
            statistic_dict[key] = 0
        statistic_dict[key] += value

print("Products in stock:")
for k, v in statistic_dict.items():
    print(f"- {k}: {v}")

print(f"Total Products: {len(statistic_dict)}")
print(f"Total Quantity: {sum(statistic_dict.values())}")
