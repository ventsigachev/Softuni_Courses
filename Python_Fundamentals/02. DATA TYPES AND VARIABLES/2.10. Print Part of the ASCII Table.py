start_index = int(input())
end_index = int(input())
character_list = list()

for i in range(start_index, end_index + 1):
    character = chr(i)
    character_list.append(character)

print(*character_list)
