num = float(input())

while True:
    if num < 1 or num > 100:
        num = float(input())
    else:
        break
print(f"The number {num} is between 1 and 100")
