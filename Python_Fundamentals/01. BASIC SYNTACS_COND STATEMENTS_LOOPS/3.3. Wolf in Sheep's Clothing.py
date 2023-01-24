input_list = [word for word in input().split(", ")]
reversed_list = input_list[::-1]

for i in range(0, len(reversed_list)):
    if reversed_list[i] == "wolf":
        if i == 0:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")
