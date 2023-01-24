A = list(range(1, 12))
B = list(range(1, 12))
card_list = [ch for ch in input().split()]

if card_list:
    for el in card_list:
        list_el = el.split("-")
        team = list_el[0]
        number = int(list_el[1])
        if team == "A":
            if number in A:
                A.remove(number)
        elif team == "B":
            if number in B:
                B.remove(number)

print(f"Team A - {len(A)}; Team B - {len(B)}")
if len(A) < 7 or len(B) < 7:
    print("Game was terminated")
