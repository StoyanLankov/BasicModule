budget = float(input())
nights = int(input())
night_price = float(input())
additional_expenses_percentage = int(input())

if nights > 7:
    night_price *= 0.95

total_nights_price = nights * night_price
additional_expenses = budget * (additional_expenses_percentage / 100)
total_expenses = total_nights_price + additional_expenses

if total_expenses <= budget:
    remaining_money = budget - total_expenses
    print(f"Ivanovi will be left with {remaining_money:.2f} leva after vacation.")
else:
    money_needed = total_expenses - budget
    print(f"{money_needed:.2f} leva needed.")
