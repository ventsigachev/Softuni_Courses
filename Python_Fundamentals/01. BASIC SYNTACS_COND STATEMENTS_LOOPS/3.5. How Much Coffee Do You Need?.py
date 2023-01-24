list_commands_lower = ["coding", "dog", "cat", "movie"]
list_commands_upper = ["CODING", "DOG", "CAT", "MOVIE"]
counter = 0

while True:
    command = input()
    if command == "END":
        break
    elif command in list_commands_lower:
        counter += 1
    elif command in list_commands_upper:
        counter += 2

if counter > 5:
    print("You need extra sleep")
else:
    print(f"{counter}")
