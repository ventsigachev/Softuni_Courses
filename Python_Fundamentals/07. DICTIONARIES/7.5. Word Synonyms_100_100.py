n = int(input())
synonyms_dict = dict()

for _ in range(n):
    key, value = input(), input()
    if key not in synonyms_dict:
        synonyms_dict[key] = []
    synonyms_dict[key].append(value)

for k, v in synonyms_dict.items():
    print(f"{k} - {', '.join(v) }")
