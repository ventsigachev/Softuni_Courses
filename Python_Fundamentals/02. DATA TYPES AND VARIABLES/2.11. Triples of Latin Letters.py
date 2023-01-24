num = int(input())

for f in range(num):
    for s in range(num):
        for t in range(num):
            print(f"{chr(97 + f)}{chr(97 + s)}{chr(97 + t)}")
