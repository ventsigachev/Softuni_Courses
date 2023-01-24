from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(y) for y in input().split(", ")]
bombs_dictionary = {40: "Datura Bombs", 60: "Cherry Bombs", 120: "Smoke Decoy Bombs"}
bombs_count_dict = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
is_successful = False

while bomb_effects and bomb_casings:
    if bombs_count_dict["Datura Bombs"] >= 3 and bombs_count_dict["Cherry Bombs"] >= 3 \
            and bombs_count_dict["Smoke Decoy Bombs"] >= 3:
        is_successful = True
        break

    first_effect = bomb_effects.popleft()
    last_casings = bomb_casings.pop()
    sum_bomb = first_effect + last_casings

    if sum_bomb in bombs_dictionary:
        key = bombs_dictionary[sum_bomb]
        bombs_count_dict[key] += 1
    else:
        bomb_effects.appendleft(first_effect)
        last_casings -= 5
        bomb_casings.append(last_casings)

if is_successful:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")

for k, v in sorted(bombs_count_dict.items()):
    print(f"{k}: {v}")
