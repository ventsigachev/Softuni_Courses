input_str = input()
result = []
[result.append(ch) if len(result) == 0 else result.append(ch) if not ch == result[-1] else None for ch in input_str]
print("".join(result))
