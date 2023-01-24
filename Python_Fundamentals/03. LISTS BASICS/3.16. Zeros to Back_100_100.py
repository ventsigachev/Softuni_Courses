numbers_list = [int(num) for num in input().split(", ")]
counter = 0
length = len(numbers_list)

for i in range(length):
    if numbers_list[i] != 0:
        numbers_list[counter] = numbers_list[i]
        counter += 1

while counter < length:
    numbers_list[counter] = 0
    counter += 1

print(numbers_list)
