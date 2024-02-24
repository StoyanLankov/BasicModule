season = input()
group_type = input()
students_count = int(input())
nights_count = int(input())

sport = ""
price_per_night = 0.0

if season == "Winter":
    if group_type == "boys":
        sport = "Judo"
        price_per_night = 9.60
    elif group_type == "girls":
        sport = "Gymnastics"
        price_per_night = 9.60
    else:
        sport = "Ski"
        price_per_night = 10.00
elif season == "Spring":
    if group_type == "boys":
        sport = "Tennis"
        price_per_night = 7.20
    elif group_type == "girls":
        sport = "Athletics"
        price_per_night = 7.20
    else:
        sport = "Cycling"
        price_per_night = 9.50
else:
    if group_type == "boys":
        sport = "Football"
        price_per_night = 15.00
    elif group_type == "girls":
        sport = "Volleyball"
        price_per_night = 15.00
    else:
        sport = "Swimming"
        price_per_night = 20.00

total_price = nights_count * students_count * price_per_night

if students_count >= 50:
    total_price *= 0.50
elif students_count >= 20:
    total_price *= 0.85
elif students_count >= 10:
    total_price *= 0.95

print(f"{sport} {total_price:.2f} lv.")
