num = int(input())

for i in range(1, num + 1):
    sum_numbers = 0
    digits = i

    while digits > 0:
        sum_numbers += digits % 10
        digits = int(digits / 10)

    if sum_numbers == 5 or sum_numbers == 7 or sum_numbers == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
