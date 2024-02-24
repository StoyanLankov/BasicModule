import math

days = int(input())
remaining_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input()) / 1000

total_food_needed = days * (dog_food_per_day + cat_food_per_day + turtle_food_per_day)
food_difference = remaining_food - math.ceil(total_food_needed)

if food_difference >= 0:
    print(f"{food_difference} kilos of food left.")
else:
    print(f"{abs(food_difference)} more kilos of food are needed.")
