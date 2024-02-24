budget = float(input())
category = input()
group_size = int(input())

ticket_price = 499.99 if category == "VIP" else 249.99

if group_size >= 1 and group_size <= 4:
    percentage = 0.75
elif group_size >= 5 and group_size <= 9:
    percentage = 0.60
elif group_size >= 10 and group_size <= 24:
    percentage = 0.50
elif group_size >= 25 and group_size <= 49:
    percentage = 0.40
else:
    percentage = 0.25

total_cost = group_size * ticket_price
transportation_cost = budget * percentage

if budget >= total_cost + transportation_cost:
    left_money = budget - (total_cost + transportation_cost)
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    needed_money = (total_cost + transportation_cost) - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")
