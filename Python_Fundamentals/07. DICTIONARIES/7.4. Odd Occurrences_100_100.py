initial_list = [word.lower() for word in input().split()]
words_dict = {word: initial_list.count(word) for word in initial_list if initial_list.count(word) % 2}
print(* words_dict)
