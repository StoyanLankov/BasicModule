target_profit = float(input())

cocktail = input()
total_income = 0

while cocktail != "Party!":
    cocktail_price = len(cocktail)
    order_quantity = int(input())

    order_price = cocktail_price * order_quantity

    if order_price % 2 != 0:
        order_price -= order_price * 0.25

    total_income += order_price

    if total_income >= target_profit:
        print("Target acquired.")
        break

    cocktail = input()

if cocktail == "Party!":
    needed_money = target_profit - total_income
    print(f"We need {needed_money:.2f} leva more.")

print(f"Club income - {total_income:.2f} leva.")
