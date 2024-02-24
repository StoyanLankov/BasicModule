days = int(input())
hours_per_day = int(input())

total_cost = 0

for day in range(1, days + 1):
    day_cost = 0
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 == 1:  # Четен ден и нечетен час
            hour_cost = 2.50
        elif day % 2 == 1 and hour % 2 == 0:  # Нечетен ден и четен час
            hour_cost = 1.25
        else:
            hour_cost = 1.00

        day_cost += hour_cost

    total_cost += day_cost
    print(f"Day: {day} - {day_cost:.2f} leva")

print(f"Total: {total_cost:.2f} leva")
