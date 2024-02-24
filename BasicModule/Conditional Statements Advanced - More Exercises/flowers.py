chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
is_holiday = input()

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0

if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

total_flowers = chrysanthemums_count + roses_count + tulips_count
total_price = (chrysanthemums_count * chrysanthemums_price) + (roses_count * roses_price) + (tulips_count * tulips_price)

if is_holiday == "Y":
    total_price *= 1.15

if season == "Spring" and tulips_count > 7:
    total_price *= 0.95

if season == "Winter" and roses_count >= 10:
    total_price *= 0.90

if total_flowers > 20:
    total_price *= 0.80

total_price += 2

print(f"{total_price:.2f}")
