input_list = [ch for ch in input()]
i = 0
explosion = 0

while True:
    try:
        input_list[i]
    except Exception:
        break
    if explosion > 0 and not input_list[i] == ">":
        del input_list[i]
        explosion -= 1
        i -= 1
    elif input_list[i] == ">":
        explosion += int(input_list[i + 1])
    i += 1

print("".join(input_list))
