size = int(input())
matrix = []
start_pos = []
is_outside = False

movements = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
food_quantity = 0

for r in range(size):
    line = [x for x in input()]
    if "S" in line:
        start_pos = [r, line.index("S")]
    matrix.append(line)

while True:
    command = input()
    if not command:
        break

    if command in movements:
        new_position = [a + b for a, b in zip(start_pos, movements[command])]
        if 0 <= new_position[0] < size and 0 <= new_position[1] < size:
            matrix[start_pos[0]][start_pos[1]] = "."
            if matrix[new_position[0]][new_position[1]] == "-":
                matrix[new_position[0]][new_position[1]] = "S"
                start_pos = new_position
            elif matrix[new_position[0]][new_position[1]] == "*":
                food_quantity += 1
                matrix[new_position[0]][new_position[1]] = "S"
                start_pos = new_position
                if food_quantity >= 10:
                    break
            elif matrix[new_position[0]][new_position[1]] == "B":
                matrix[new_position[0]][new_position[1]] = "."
                sec_pos = [(a, b) for a in range(len(matrix)) for b in range(len(matrix[a])) if matrix[a][b] == "B"]
                sec_b_pos = [sec_pos[0][0], sec_pos[0][1]]
                matrix[sec_b_pos[0]][sec_b_pos[1]] = "S"
                start_pos = sec_b_pos

        else:
            matrix[start_pos[0]][start_pos[1]] = "."
            is_outside = True
            break

if is_outside:
    print("Game over!")

if food_quantity >= 10:
    print("You won! You fed the snake.")

print(f"Food eaten: {food_quantity}")

[print("".join(el for el in row)) for row in matrix]
