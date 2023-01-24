string_to_check = input().lower()
words_to_check_list = ["sand", "water", "fish", "sun"]
counter = 0

for word in words_to_check_list:
    counter += string_to_check.count(word)

print(counter)
