r, c = [int(n) for n in input().split()]
pal_matrix = [[f"{chr(i)}{chr(i + x)}{chr(i)}" for x in range(c)] for i in range(97, 97 + r)]
[print(" ".join(y)) for y in pal_matrix]
