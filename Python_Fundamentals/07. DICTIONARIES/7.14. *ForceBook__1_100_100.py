force_book_dict = dict()
result = ''
no_player = True

while True:
    data = input()
    if data == 'Lumpawaroo':
        break
    if "|" in data:
        side, player = data.split(" | ")[0], data.split(" | ")[1]
        for pls in force_book_dict.values():
            if player in pls:
                no_player = False
        if no_player:
            if side not in force_book_dict:
                force_book_dict[side] = []
            force_book_dict[side].append(player)
    elif "->" in data:
        player, side = data.split(" -> ")[0], data.split(" -> ")[1]
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
