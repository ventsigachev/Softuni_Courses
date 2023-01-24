string = input()
list_string = list(string)
index_list = list()

for i in range(0, len(list_string)):
    if list_string[i].isupper():
        index_list.append(i)

print(index_list)
