def palindrome(text, ind=0):
    if ind == len(text) // 2:
        return f"{text} is a palindrome"
    if not text[ind] == text[len(text) - 1 - ind]:
        return f"{text} is not a palindrome"
    return palindrome(text, ind + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))

