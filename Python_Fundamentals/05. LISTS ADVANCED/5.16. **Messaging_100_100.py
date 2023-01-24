list_num = [num for num in input().split()]
list_text = [ch for ch in input()]
list_indexes = []
string = ''

for el in list_num:
    result = 0
    for x in el:
        result += int(x)
    list_indexes.append(result)

ind = 0

for idx in list_indexes:
    if idx > len(list_text):
        idx -= 2
        ind = -idx
    else:
        ind = idx
    string += list_text.pop(ind)

print(string)
