checking_dict = {"{": "}", "[": "]", "(": ")"}
checker = ["}", "]", ")"]
stack = []
is_valid = True
in_string = input()

for st in in_string:
    if st in checking_dict:
        stack.append(st)
    elif st in checker:
        if stack:
            if checking_dict[stack[-1]] == st:
                stack.pop()
            else:
                is_valid = False
                break
        else:
            is_valid = False

if is_valid:
    print("YES")
else:
    print("NO")
