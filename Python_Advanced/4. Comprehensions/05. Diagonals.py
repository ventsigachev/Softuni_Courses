num_matrix = [[int(n) for n in input().split(", ")] for _ in range(int(input()))]
f_d = [num_matrix[f][f] for f in range(len(num_matrix))]
s_d = [num_matrix[s][len(num_matrix) - s - 1] for s in range(len(num_matrix))]
print(f"First diagonal: {', '.join([str(x) for x in f_d])}. Sum: {sum(f_d)}")
print(f"Second diagonal: {', '.join([str(y) for y in s_d])}. Sum: {sum(s_d)}")
