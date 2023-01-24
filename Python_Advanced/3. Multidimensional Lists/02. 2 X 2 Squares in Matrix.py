rows, cols = [int(n) for n in input().split()]
matrix = []
count = 0

for _ in range(rows):
    matrix.append(input().split())

for r in range(rows - 1):
    for c in range(cols - 1):
        upper_left = matrix[r][c]
        upper_right = matrix[r][c + 1]
        lower_left = matrix[r + 1][c]
        lower_right = matrix[r + 1][c + 1]
        if upper_left == upper_right == lower_left == lower_right:
            count += 1

print(count)
