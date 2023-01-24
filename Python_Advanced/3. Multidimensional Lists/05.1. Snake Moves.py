from collections import deque

rows, cols = [int(num) for num in input().split()]
deque_chars = deque(input())
matrix = []

for _ in range(rows):
    matrix.append(["" for _ in range(cols)])

for r in range(rows):
    for c in range(cols):
        active = c
        char = deque_chars.popleft()
        if not r % 2 == 0:
            active = cols - 1 - c
        matrix[r][active] = char
        deque_chars.append(char)

for row in matrix:
    print("".join(row))
