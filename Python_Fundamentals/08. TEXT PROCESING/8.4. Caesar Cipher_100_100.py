input_str = input()
result = [chr(ord(ch) + 3) for ch in input_str]
print("".join(result))
