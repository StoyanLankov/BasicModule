# Read user input
number = int(input())

bonus_points = 0

# Logic

if number <= 100:
    bonus_points = 5
elif number > 1000:
    bonus_points = number * 0.10
else:
    bonus_points = 0.20 * number

if number % 2 == 0:
    bonus_points += 1
elif number % 10 == 5:
    bonus_points += 2

total_sum = bonus_points + number
# Print output
print(bonus_points)
print(total_sum)