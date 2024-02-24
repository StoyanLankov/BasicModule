season = input()
kilometers_per_month = float(input())

salary_per_km = 0.0

if season == "Spring" or season == "Autumn":
    if kilometers_per_month <= 5000:
        salary_per_km = 0.75
    elif kilometers_per_month <= 10000:
        salary_per_km = 0.95
    else:
        salary_per_km = 1.45
elif season == "Summer":
    if kilometers_per_month <= 5000:
        salary_per_km = 0.90
    elif kilometers_per_month <= 10000:
        salary_per_km = 1.10
    else:
        salary_per_km = 1.45
else:  # Winter season
    if kilometers_per_month <= 5000:
        salary_per_km = 1.05
    elif kilometers_per_month <= 10000:
        salary_per_km = 1.25
    else:
        salary_per_km = 1.45

total_salary = 4 * kilometers_per_month * salary_per_km
total_salary -= 0.1 * total_salary

print(f"{total_salary:.2f}")
