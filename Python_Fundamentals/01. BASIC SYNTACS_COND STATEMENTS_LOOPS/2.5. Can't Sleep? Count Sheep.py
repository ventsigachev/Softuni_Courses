num = int(input())

if num == 0:
    print("0 sheep...")
else:
    for i in range(1, num + 1):
        print(f"{i} sheep...", end="")
