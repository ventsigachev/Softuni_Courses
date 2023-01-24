courses_dict = dict()
result = ''

while True:
    data = input().split(" : ")
    if data[0] == 'end':
        break
    c_n, st_n = data[0], data[1]
    if c_n not in courses_dict:
        courses_dict[c_n] = []
    if st_n not in courses_dict[c_n]:
        courses_dict[c_n].append(st_n)

for k, vs in sorted(courses_dict.items(), key=lambda x: -len(x[1])):
    result += f"{k}: {len(vs)}\n"
    for v in sorted(vs):
        result += f"-- {v}\n"

print(result)
