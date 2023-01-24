input_names = input().split(", ")
valid_names = []
[valid_names.append(name) for name in input_names
 if 3 <= len(name) <= 16 and (name.isalnum() or "_" in name or "-" in name)]
[print(name) for name in valid_names]
