initial_list = [ch for ch in input().split("|")]
budget = float(input())
temp_budget = budget

prices_final_list = list()

for el in initial_list:
    el_list = el.split('->')
    item_type = el_list[0]
    item_price = float(el_list[1])
    if item_type == 'Clothes':
        if item_price <= 50 and item_price <= temp_budget:
            prices_final_list.append(item_price)
            temp_budget -= item_price
    elif item_type == 'Shoes':
        if item_price <= 35 and item_price <= temp_budget:
            prices_final_list.append(item_price)
            temp_budget -= item_price
    elif item_type == 'Accessories':
        if item_price <= 20.50 and item_price <= temp_budget:
            prices_final_list.append(item_price)
            temp_budget -= item_price

for i in range(len(prices_final_list)):
    prices_final_list[i] += prices_final_list[i] * 40 / 100

all_sum = sum(prices_final_list) + temp_budget
profit = all_sum - budget

for num in prices_final_list:
    print(f"{num:.2f}", end=' ')

print(f"\nProfit: {profit:.2f}")

if all_sum >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
