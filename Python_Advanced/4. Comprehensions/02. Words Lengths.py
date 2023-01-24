d_text = {x: len(x) for x in input().split(", ")}
print(", ".join([f"{k} -> {v}" for k, v in d_text.items()]))
