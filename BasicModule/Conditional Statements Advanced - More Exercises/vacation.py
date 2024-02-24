budget = float(input())
season = input()

accommodation = ""
location = ""
price_percentage = 0.0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        price_percentage = 0.65
    else:
        location = "Morocco"
        price_percentage = 0.45
elif budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        price_percentage = 0.80
    else:
        location = "Morocco"
        price_percentage = 0.60
else:
    accommodation = "Hotel"
    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"
    price_percentage = 0.90

total_price = budget * price_percentage

print(f"{location} - {accommodation} - {total_price:.2f}")
