tournament_count = int(input())
starting_points = int(input())

total_points = 0
wins = 0

for i in range(tournament_count):
    result = input()

    if result == "W":
        total_points += 2000
        wins += 1
    elif result == "F":
        total_points += 1200
    elif result == "SF":
        total_points += 720

average_points = total_points // tournament_count
total_points += starting_points
win_percentage = (wins / tournament_count) * 100

print(f"Final points: {total_points}")
print(f'Average points: {average_points}')
print(f"{win_percentage:.2f}%")
