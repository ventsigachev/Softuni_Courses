students_dict = dict()

for _ in range(int(input())):
    name, grade = input(), float(input())
    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(grade)

for k, vs in students_dict.items():
    aver = sum(vs) / len(vs)
    students_dict[k] = aver

for name, value in sorted(students_dict.items(), key=lambda x: -x[1]):
    if value >= 4.50:
        print(f"{name} -> {value:.2f}")
