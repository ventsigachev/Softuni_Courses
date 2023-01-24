import re

pattern = r"^>>([a-zA-Z]+)<<([0-9]+\.?[0-9]+)!([0-9]+)$"

furniture = list()
all_money = 0

while True:
    line = input()
    if line == "Purchase":
        break
    match = re.match(pattern, line)
    if match:
        name = match.group(1)
        price = float(match.group(2))
        quantity = int(match.group(3))
        furniture.append(name)
        all_money += price * quantity

print("Bought furniture:")
for f in furniture:
    print(f"{f}")
print(f"Total money spend: {all_money:.2f}")
