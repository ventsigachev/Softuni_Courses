dict_bunker = {x: [] for x in input().split(", ")}
t_quantity = 0
t_quality = 0
num = int(input())

for _ in range(num):
    c, i, q_a_q = input().split(" - ")
    quantity = int(q_a_q.split(";")[0].split(":")[1])
    quality = int(q_a_q.split(";")[1].split(":")[1])
    if c in dict_bunker:
        dict_bunker[c].append(i)
        t_quantity += quantity
        t_quality += quality

print(f"Count of items: {t_quantity}\nAverage quality: {t_quality/len(dict_bunker):.2f}")
[print(f"{k} -> {', '.join(dict_bunker[k])}") for k in dict_bunker]
