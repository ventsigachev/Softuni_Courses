import re

pattern = r"\b[_][0-9A-Za-z]+\b"

line = input()
matches = re.findall(pattern, line)
matches = [match.replace("_", "") for match in matches]
print(",".join(matches))
