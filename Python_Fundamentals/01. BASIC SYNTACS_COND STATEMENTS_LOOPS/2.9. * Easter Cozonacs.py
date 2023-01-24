budget = float(input())
price_flour = float(input())

price_pack_eggs = 75 / 100 * price_flour
price_litter_milk = price_flour + 25 / 100 * price_flour
current_price_milk = price_litter_milk / 4
price_cozonac = price_flour + price_pack_eggs + current_price_milk

colored_eggs_count = 0
cozonac_count = 0

while True:
    if budget < price_cozonac:
        break
    budget_left = budget - price_cozonac
    budget = budget_left
    cozonac_count += 1
    colored_eggs_count += 3
    if cozonac_count % 3 == 0:
        counter_eggs = cozonac_count - 2
        colored_eggs_count -= counter_eggs


print(f"You made {cozonac_count} cozonacs! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")
