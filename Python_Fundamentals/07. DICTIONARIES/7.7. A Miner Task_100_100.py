miner_dict = dict()

while True:
    key = input()
    if key == "stop":
        break
    value = int(input())
    if key not in miner_dict:
        miner_dict[key] = 0
    miner_dict[key] += value

for k, v in miner_dict.items():
    print(f"{k} -> {v}")
