from collections import deque

rows, cols = [int(num) for num in input().split()]
deque_chars = deque(input())
matrix = []

for _ in range(rows):
    matrix.append(["" for _ in range(cols)])

for r in range(rows):
    if r % 2 == 0:
        for c in range(cols):
            current = deque_chars.popleft()
            matrix[r][c] = current
            deque_chars.append(current)
    else:
        for c in range(cols - 1, -1, -1):
            current = deque_chars.popleft()
            matrix[r][c] = current
            deque_chars.append(current)

for row in matrix:
    print("".join(row))
