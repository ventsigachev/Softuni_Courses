matrix = [[int(n) for n in input().split(" ")] for _ in range(int(input()))]

while True:
    t = input().split()
    if t[0] == "END":
        break
    r, c, v = int(t[1]), int(t[2]), int(t[3])
    if not 0 <= r < len(matrix) or not 0 <= c < len(matrix):
        print("Invalid coordinates")
        continue
    elif t[0] == "Add":
        matrix[r][c] += v
    elif t[0] == "Subtract":
        matrix[r][c] -= v

[print(*row) for row in matrix]
