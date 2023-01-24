text = input().split()
f_text = [x for x in text if len(x) % 2 == 0]
[print(y) for y in f_text]
