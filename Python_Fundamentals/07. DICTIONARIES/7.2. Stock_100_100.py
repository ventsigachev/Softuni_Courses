initial_list = input().split()
check_list = input().split()
stock_dict = dict()

for i in range(0, len(initial_list), 2):
    key = initial_list[i]
    value = initial_list[i + 1]
    stock_dict[key] = int(value)

for el in check_list:
    if el in stock_dict:
        print(f"We have {stock_dict[el]} of {el} left")
    else:
        print(f"Sorry, we don't have {el}")
