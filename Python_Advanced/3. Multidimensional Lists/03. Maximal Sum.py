import sys

rows, cols = [int(num) for num in input().split()]
rectangular_matrix = []
final_matrix = []
final_sum = -sys.maxsize - 1

for _ in range(rows):
    rectangular_matrix.append([int(x) for x in input().split()])

for r in range(rows - 2):
    for c in range(cols - 2):
        matrix = []
        matrix_sum = 0
        r_ind = 0
        for m_r in range(r, r + 3):
            matrix.append([])
            for m_c in range(c, c + 3):
                matrix[r_ind].append(rectangular_matrix[m_r][m_c])
                matrix_sum += rectangular_matrix[m_r][m_c]
            r_ind += 1
        if matrix_sum > final_sum:
            final_sum = matrix_sum
            final_matrix = matrix

print(f"Sum = {final_sum}")
for row in final_matrix:
    print(" ".join([str(y) for y in row]))
