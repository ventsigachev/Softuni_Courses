number_of_snowballs = int(input())
end_value = 0
end_snowball_snow = 0
end_snowball_time = 0
end_snowball_quality = 0

for i in range(number_of_snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = (snowball_snow // snowball_time) ** snowball_quality
    if value >= end_value:
        end_value = value
        end_snowball_snow = snowball_snow
        end_snowball_time = snowball_time
        end_snowball_quality = snowball_quality

print(f"{end_snowball_snow} : {end_snowball_time} = {end_value:.0f} ({end_snowball_quality})")
