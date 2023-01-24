num = int(input())

for a in range(1, num + 1):
    for b in range(0, a):
        print("*", end="")
    print()
for c in range(num - 1, -1, -1):
    for d in range(0, c):
        print("*", end="")
    print()
