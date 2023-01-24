initial_energy = 100
initial_coins = 100
events_list = [e for e in input().split('|')]
checker = len(events_list)
counter = 0

for e in events_list:
    counter += 1
    e_list = e.split("-")
    name = e_list[0]
    number = int(e_list[1])
    if name == 'rest':
        if number + initial_energy > 100:
            print("You gained 0 energy.")
            print(f"Current energy: {initial_energy}.")
        else:
            initial_energy += number
            print(f"You gained {number} energy.")
            print(f"Current energy: {initial_energy}.")
    elif name == 'order':
        initial_energy -= 30
        if initial_energy > 0:
            initial_coins += number
            print(f"You earned {number} coins.")

        elif initial_energy < 0:
            initial_energy += 50
            print("You had to rest!")
    else:
        if initial_coins - number > 0:
            initial_coins -= number
            print(f"You bought {name}.")
        else:
            print(f"Closed! Cannot afford {name}.")
            break

if counter == checker:
    print(f"Day completed!\nCoins: {initial_coins}\nEnergy: {initial_energy}")
