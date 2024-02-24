budget = int(input())
season = input()
numbers_of_fisherman = int(input())
boat_price = 0

if season == 'Spring':
    boat_price = 3000
elif season == 'Summer' or season == 'Autumn':
    boat_price = 4200
elif season == 'Winter':
    boat_price = 2600

if numbers_of_fisherman <= 6:
    boat_price *= 0.9
elif numbers_of_fisherman <= 11:
    boat_price *= 0.85
elif numbers_of_fisherman > 12:
    boat_price *= 0.75

if numbers_of_fisherman % 2 == 0 and season != 'Autumn':
    boat_price *= 0.95

difference = abs(boat_price - budget)

if budget >= boat_price:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')