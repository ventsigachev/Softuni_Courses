fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

lost_helmets = fights // 2
lost_swords = fights // 3
lost_shields = fights // 6
lost_armors = lost_shields // 2

lost_helmets_sum = helmet_price * lost_helmets
lost_swords_sum = lost_swords * sword_price
lost_shields_sum = shield_price * lost_shields
lost_armor_sum = armor_price * lost_armors

end_sum = lost_armor_sum + lost_helmets_sum + lost_shields_sum + lost_swords_sum

print(f"Gladiator expenses: {end_sum:.2f} aureus")
