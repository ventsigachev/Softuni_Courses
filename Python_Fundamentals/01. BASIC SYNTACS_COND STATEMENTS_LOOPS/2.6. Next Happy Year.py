year = int(input()) + 1

while True:
    if len(set(str(year))) == len(str(year)):
        print(year)
        break
    else:
        year += 1
