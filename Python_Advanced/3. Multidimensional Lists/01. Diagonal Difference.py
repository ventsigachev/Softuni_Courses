m_size = int(input())
matrix = []
p_d_sum = 0
s_d_sum = 0


for _ in range(m_size):
    matrix.append([int(num) for num in input().split()])

for i in range(len(matrix)):
    p_d_sum += matrix[i][i]
    s_d_sum += matrix[i][m_size - i - 1]

diff = abs(p_d_sum - s_d_sum)
print(diff)
