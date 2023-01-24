with open("text.txt", "r") as f:
    result = ""

    for num, line in enumerate(f, start=1):
        count_a = 0
        count_p = 0
        for el in line:
            if el.isalpha():
                count_a += 1
            elif el in "-,.!?\'":
                count_p += 1
        result += f"Line {num}: {line[:-2]} ({count_a})({count_p})\n"

with open("output.txt", "w") as output:
    output.write(result)
