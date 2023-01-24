def get_kills(row, col, mat):
    num_kills = 0
    if row - 2 >= 0 and col - 1 >= 0:
        if mat[row - 2][col - 1] == "K":
            num_kills += 1
    if row - 2 >= 0 and col + 1 < len(mat) and mat[row - 2][col + 1] == "K":
        num_kills += 1
    if row - 1 >= 0 and col - 2 >= 0 and mat[row - 1][col - 2] == "K":
        num_kills += 1
    if row - 1 >= 0 and col + 2 < len(mat) and mat[row - 1][col + 2] == "K":
        num_kills += 1
    if row + 1 < len(mat) and col - 2 >= 0 and mat[row + 1][col - 2] == "K":
        num_kills += 1
    if row + 1 < len(mat) and col + 2 < len(mat) and mat[row + 1][col + 2] == "K":
        num_kills += 1
    if row + 2 < len(mat) and col - 1 >= 0 and mat[row + 2][col - 1] == "K":
        num_kills += 1
    if row + 2 < len(mat) and col + 1 < len(mat) and mat[row + 2][col + 1] == "K":
        num_kills += 1

    return num_kills


rows = int(input())
matrix = []
all_kills = 0

for _ in range(rows):
    matrix.append([char for char in input()])

while True:
    best_kills = 0
    best_kills_spot = []
    for r in range(rows):
        for c in range(rows):
            active = matrix[r][c]
            if active == "K":
                kills = get_kills(r, c, matrix)
                if kills > best_kills:
                    best_kills = kills
                    best_kills_spot = [r, c]
    if not best_kills:
        break
    matrix[best_kills_spot[0]][best_kills_spot[1]] = "0"
    all_kills += 1

print(all_kills)
