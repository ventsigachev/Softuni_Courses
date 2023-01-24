text_dict = dict()
input_list = [ch for ch in input() if not ch == " "]

for ch in input_list:
    if ch not in text_dict:
        text_dict.update({ch: 0})
    text_dict[ch] += 1

for k, v in text_dict.items():
    print(f"{k} -> {v}")
