phb_dict = dict()

while True:
    text = input().split("-")
    if len(text) == 1:
        break
    phb_dict[text[0]] = text[1]

for _ in range(int(text[0])):
    name = input()
    if name in phb_dict:
        print(f"{name} -> {phb_dict[name]}")
    else:
        print(f"Contact {name} does not exist.")
