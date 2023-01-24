force_book_dict = dict()
result = ''

while True:
    data = input()
    if data == 'Lumpawaroo':
        break

    if "|" in data:
        data = data.split(" | ")
        side = data[0]
        player = data[1]
        if side not in force_book_dict:
            force_book_dict[side] = []
        if player not in force_book_dict[side]:
            force_book_dict[side].append(player)
    elif "->" in data:
        data = data.split(" -> ")
        side = data[1]
        player = data[0]
        for k, vs in force_book_dict.items():
            if player in vs:
                force_book_dict[k].remove(player)
        if side not in force_book_dict:
            force_book_dict[side] = []
        force_book_dict[side].append(player)
        result += f"{player} joins the {side} side!\n"

for side, pls in sorted(force_book_dict.items(), key=lambda x: (-len(x[1]), x[0])):
    if pls:
        result += f"Side: {side}, Members: {len(pls)}\n"
        for pl in sorted(pls):
            result += f"! {pl}\n"

print(result)
