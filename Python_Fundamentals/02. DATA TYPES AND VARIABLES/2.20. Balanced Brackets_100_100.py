num = int(input())
opening_count = 0
closing_count = 0

is_opened = False
is_balanced = True

for i in range(num):
    string = input()
    if is_opened and string == "(":
        print("UNBALANCED")
        is_balanced = False
        break
    else:
        is_opened = False
    if string == "(":
        opening_count += 1
        is_opened = True
    elif string == ")":
        closing_count += 1
    if input == "(" and i == num - 1:
        print("UNBALANCED")
        is_balanced = False
        break

if is_balanced:
    if opening_count == closing_count:
        print("BALANCED")
    else:
        print("UNBALANCED")
