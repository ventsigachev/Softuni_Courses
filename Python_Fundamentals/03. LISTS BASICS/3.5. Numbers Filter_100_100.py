original_list = list()
final_list = list()

lines = int(input())

for l in range(lines):
    num = int(input())
    original_list.append(num)

command = input()

if command == 'even':
    for num in original_list:
        if num % 2 == 0:
            final_list.append(num)
elif command == 'odd':
    for num in original_list:
        if num % 2 == 1:
            final_list.append(num)
elif command == 'positive':
    for num in original_list:
        if num >= 0:
            final_list.append(num)
elif command == 'negative':
    for num in original_list:
        if num < 0:
            final_list.append(num)

print(final_list)
