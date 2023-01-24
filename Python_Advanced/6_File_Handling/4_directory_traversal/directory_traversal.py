import os

p_to_files = input()
needed_separators = p_to_files.count(os.path.sep)
dict_to_print = {}
to_report = ''

for root, dirs, files in os.walk(p_to_files, topdown=False):
    if needed_separators - root.count(os.path.sep) > 1:
        continue
    for file in files:
        file_ext = file.split(".")[-1]
        if file_ext not in dict_to_print:
            dict_to_print[file_ext] = []
        dict_to_print[file_ext].append(file)

for k, v in sorted(dict_to_print.items()):
    to_report += f".{k}\n"
    for el in sorted(v):
        to_report += f"- - - {el}\n"

desktop = os.path.expanduser("~/Desktop")
file_location = desktop + os.path.sep + 'report.txt'

with open(file_location, 'w') as report:
    report.write(to_report)
