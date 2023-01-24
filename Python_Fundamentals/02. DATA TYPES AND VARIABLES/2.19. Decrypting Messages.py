key = int(input())
num_of_lines = int(input())

result = ''

for i in range(num_of_lines):
    ord_char = int(ord(input()))
    result += chr(ord_char + key)

print(result)
