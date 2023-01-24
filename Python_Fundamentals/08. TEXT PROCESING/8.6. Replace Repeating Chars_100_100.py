input_str = input()
result = ""

for ch in input_str:
    if len(result) == 0:
        result += ch
    else:
        if not ch == result[-1]:
            result += ch
print(result)
