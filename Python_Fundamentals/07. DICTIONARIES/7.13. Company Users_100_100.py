companies_dict = dict()
result = ''

while True:
    data = input().split(" -> ")
    if data[0] == "End":
        break
    name, ids = data[0], data[1]
    if name not in companies_dict:
        companies_dict[name] = []
    if ids not in companies_dict[name]:
        companies_dict[name].append(ids)

for company, ids in sorted(companies_dict.items()):
    result += f"{company}\n"
    for v in ids:
        result += f"-- {v}\n"

print(result)
