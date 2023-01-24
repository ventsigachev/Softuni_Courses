students_dict = dict()
languages_dict = dict()
result = ''

while True:
    data = input().split("-")
    if data[0] == "exam finished":
        break
    elif len(data) == 3:
        name, lang, score = data[0], data[1], int(data[2])
        if lang not in languages_dict:
            languages_dict[lang] = 0
        languages_dict[lang] += 1
        if name not in students_dict:
            students_dict[name] = 0
        if students_dict[name] <= score:
            students_dict[name] = score
    elif len(data) == 2 and data[1] == "banned":
        cheater = data[0]
        if cheater in students_dict:
            del students_dict[cheater]

result += "Results:\n"
for k, v in sorted(students_dict.items(), key=lambda a: (-a[1], a[0])):
    result += f"{k} | {v}\n"
result += "Submissions:\n"
for x, y in sorted(languages_dict.items(), key=lambda b: (-b[1], b[0])):
    result += f"{x} - {y}\n"
print(result)
