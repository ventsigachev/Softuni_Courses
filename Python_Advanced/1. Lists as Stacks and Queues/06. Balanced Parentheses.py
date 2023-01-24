from collections import deque

checking_dict = {"{": "}", "[": "]", "(": ")"}
d_parentheses = deque()
is_valid = True
[d_parentheses.append(el) for el in input()]

while d_parentheses:
    f_el, l_el = d_parentheses.popleft(), d_parentheses.pop()
    if f_el not in checking_dict.keys() or not l_el == checking_dict[f_el]:
        is_valid = False
        break

if is_valid:
    print("YES")
else:
    print("NO")
