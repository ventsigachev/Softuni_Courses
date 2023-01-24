countries = input().split(", ")
capitals = input().split(", ")
d_c_c = dict(zip(countries, capitals))
[print(f"{k} -> {v}") for k, v in d_c_c.items()]
