num = int(input())
opening_count = 0
closing_count = 0
o_i = 0
c_i = 0

for i in range(1, num + 1):
    char = input()
    if char == "(":
        opening_count += 1
        o_i += i
    elif char == ")":
        closing_count += 1
        c_i += i

if opening_count == closing_count and o_i < c_i:
    print("BALANCED")
else:
    print("UNBALANCED")
