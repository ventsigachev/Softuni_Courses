string_1, string_2 = input().split()
result = 0

for i in range(max(len(string_1), len(string_2))):
    if i < len(string_1) and i < len(string_2):
        result += ord(string_1[i]) * ord(string_2[i])
    else:
        if i < len(string_1):
            result += ord(string_1[i])
        elif i < len(string_2):
            result += ord(string_2[i])
print(result)
