char_dict = dict()

for ch in input():
    if ch not in char_dict:
        char_dict[ch] = 0
    char_dict[ch] += 1

for k, v in sorted(char_dict.items()):
    print(f"{k}: {v} time/s")
