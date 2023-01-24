string_1 = input()
string_2 = input()
old_string = string_1

for i in range(0, len(string_1)):
    current_string = ""
    for a in range(0, i + 1):
        char_2 = string_2[a]
        current_string += char_2
    for b in range(i + 1, len(string_1)):
        char_1 = string_1[b]
        current_string += char_1
    if not current_string == old_string:
        print(current_string)
        old_string = current_string
