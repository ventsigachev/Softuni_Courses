lines = int(input())
word = input()
list_of_strings = list()

for l in range(lines):
    string = input()
    list_of_strings.append(string)
print(list_of_strings)

for i in range(len(list_of_strings) - 1, -1, -1):
    if word not in list_of_strings[i]:
        list_of_strings.pop(i)
print(list_of_strings)
