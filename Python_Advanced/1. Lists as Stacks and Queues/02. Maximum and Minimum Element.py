r = int(input())
stack = []

for _ in range(r):
    pairs = input().split()
    act = int(pairs[0])

    if act == 1:
        stack.append(int(pairs[1]))
    elif act == 2 and stack:
        stack.pop()
    elif act == 3 and stack:
        print(max(stack))
    elif act == 4 and stack:
        print(min(stack))

print(", ".join(str(x) for x in stack[::-1]))
