import re

text = input()
checker = input()

pattern = f"\\b{checker}\\b"

matches = len(re.findall(pattern, text, re.I))

print(matches)
