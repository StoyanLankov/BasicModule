money = float(input())
year = int(input())

ivan_years = 17
money_spent = 12000

for i in range(1800, year + 1):
    ivan_years += 1
    if i % 2 == 0:
        money -= money_spent
    else:
        money -= money_spent + 50 * ivan_years

if money >= 0:
    print(f'Yes! He will live a carefree life and will have {money:.2f} dollars left.')
else:
    print(f'He will need {abs(money):.2f} dollars to survive.')