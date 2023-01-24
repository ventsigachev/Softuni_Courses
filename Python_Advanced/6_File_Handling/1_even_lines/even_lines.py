with open("text.txt", "r") as file:
    for i, str_ in enumerate(file):
        if i % 2 == 0:
            for el in "-,.!?":
                str_ = str_.replace(el, "@")
            rev_line = str_.split()[::-1]
            print(*rev_line)
