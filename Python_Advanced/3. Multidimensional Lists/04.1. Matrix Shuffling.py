rows, cols = [int(num) for num in input().split()]
r_matrix = []

for _ in range(rows):
    r_matrix.append([x for x in input().split()])

while True:
    a_swap = []
    b_swap = []
    text = input().split()
    if text[0] == "END":
        break
    if text[0] == "swap" and len(text) == 5:
        if 0 <= int(text[1]) < rows and 0 <= int(text[2]) < cols:
            a_swap = [int(text[1]), int(text[2])]
        if 0 <= int(text[3]) < rows and 0 <= int(text[4]) < cols:
            b_swap = [int(text[3]), int(text[4])]
        if a_swap and b_swap:
            r_matrix[a_swap[0]][a_swap[1]], r_matrix[b_swap[0]][b_swap[1]] = r_matrix[b_swap[0]][b_swap[1]], \
                                                                             r_matrix[a_swap[0]][a_swap[1]]

            for r in r_matrix:
                print(" ".join(r))
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
