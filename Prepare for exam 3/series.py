# Read input
budget = float(input())
num_series = int(input())

series_discounts = {
    "Thrones": 0.5,
    "Lucifer": 0.4,
    "Protector": 0.3,
    "TotalDrama": 0.2,
    "Area": 0.1
}

total_price = 0

for _ in range(num_series):
    series_name = input()
    series_price = float(input())

    if series_name in series_discounts:
        series_price *= (1 - series_discounts[series_name])

    total_price += series_price

if total_price <= budget:
    remaining_money = budget - total_price
    print(f"You bought all the series and left with {remaining_money:.2f} lv.")
else:
    needed_money = total_price - budget
    print(f"You need {needed_money:.2f} lv. more to buy the series!")
