palindromes_list = [word for word in input().split() if word == word[::-1]]

print(f"{palindromes_list}\nFound palindrome {palindromes_list.count(input())} times")
