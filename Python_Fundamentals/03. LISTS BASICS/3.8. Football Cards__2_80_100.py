team_a = 11
team_b = 11

list_players_off_a = list()
list_players_off_b = list()

input_list = [ch for ch in input().split()]

for el in input_list:
    list_el = el.split("-")
    if list_el[0] == "A" and list_el[1] not in list_players_off_a:
        if team_a >= 7:
            team_a -= 1
            list_players_off_a.append(list_el[1])
    elif list_el[0] == "B" and list_el[1] not in list_players_off_b:
        if team_b >= 7:
            team_b -= 1
            list_players_off_b.append(list_el[1])

print(f"Team A - {team_a}; Team B - {team_b}")
if team_a < 7 or team_b < 7:
    print("Game was terminated")
