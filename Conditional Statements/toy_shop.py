# Read user input
price_of_holiday = float(input())
number_puzzle = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

# Logic

price_of_puzzle = number_puzzle * 2.60
price_of_dolls = number_dolls * 3
price_of_bears = number_bears * 4.10
price_of_minions = number_minions * 8.20
price_of_trucks = number_trucks * 2

total_price_toys = price_of_puzzle + price_of_dolls + price_of_bears + price_of_minions + price_of_trucks
total_number = number_puzzle + number_dolls + number_bears + number_minions + number_trucks

if total_number >= 50:
    total_price_toys *= 0.75

total_price_toys *= 0.90

left_money = abs(total_price_toys - price_of_holiday)

if total_price_toys >= price_of_holiday:
    print(f'Yes! {left_money:.2f} lv left.')
else:
    print(f'Not enough money! {left_money:.2f} lv needed.')
