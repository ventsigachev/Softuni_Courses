legendary_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_dict = dict()
is_winner = False
result = ''

while True:
    if is_winner:
        break
    data = input().split()

    for i in range(0, len(data), 2):
        value = int(data[i])
        key = data[i + 1].lower()
        if key in legendary_dict:
            legendary_dict[key] += value
        else:
            if key not in junk_dict:
                junk_dict[key] = 0
            junk_dict[key] += value

        if legendary_dict['shards'] >= 250:
            is_winner = True
            result += "Shadowmourne obtained!\n"
            legendary_dict['shards'] -= 250
            break
        if legendary_dict['fragments'] >= 250:
            is_winner = True
            result += "Valanyr obtained!\n"
            legendary_dict['fragments'] -= 250
            break
        if legendary_dict['motes'] >= 250:
            is_winner = True
            result += "Dragonwrath obtained!\n"
            legendary_dict['motes'] -= 250
            break

for k, v in sorted(legendary_dict.items(), key=lambda x: (-x[1], x[0])):
    result += f"{k}: {v}\n"

for k, v in sorted(junk_dict.items()):
    result += f"{k}: {v}\n"

print(result)
