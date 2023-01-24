input_str = input()
[print(f":{input_str[i + 1]}") for i in range(len(input_str)) if input_str[i] == ":"]
