intersection = set()

for _ in range(int(input())):
    borders = input().split("-")
    f_b = borders[0].split(",")
    f_set = {x for x in range(int(f_b[0]), int(f_b[1]) + 1)}
    s_b = borders[1].split(",")
    s_set = {y for y in range(int(s_b[0]), int(s_b[1]) + 1)}

    current_intersection = f_set.intersection(s_set)
    if len(intersection) < len(current_intersection):
        intersection = current_intersection

printing_list = list(map(str, intersection))
print(f"Longest intersection is [{', '.join(printing_list)}] with length {len(printing_list)}")
