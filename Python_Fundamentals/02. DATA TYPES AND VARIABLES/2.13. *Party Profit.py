import math

number_of_people = int(input())
days = int(input())
earning_coins = 50 * days

for day in range(1, days + 1):
    if day % 10 == 0:
        number_of_people -= 2
    if day % 15 == 0:
        number_of_people += 5
    if day % 3 == 0:
        earning_coins -= 3 * number_of_people
    if day % 5 == 0:
        earning_coins += 20 * number_of_people
        if day % 3 == 0:
            earning_coins -= 2 * number_of_people
    earning_coins -= 2 * number_of_people

coins_each = math.floor(earning_coins / number_of_people)
print(f"{number_of_people} companions received {coins_each} coins each.")
