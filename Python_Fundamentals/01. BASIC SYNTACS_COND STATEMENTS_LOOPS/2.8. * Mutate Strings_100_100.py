list_1 = list(input())
list_2 = list(input())

for i in range(len(list_1)):
    a = list_1[i]
    b = list_2[i]
    if a != b:
        list_1[i] = b
        print(''.join(list_1))
