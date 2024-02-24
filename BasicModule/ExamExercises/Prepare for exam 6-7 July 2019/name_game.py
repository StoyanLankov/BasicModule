winner_name = ""
winner_points = 0

while True:
    player_name = input()

    if player_name == "Stop":
        break

    player_points = 0

    for _ in range(len(player_name)):
        num = int(input())
        letter = player_name[_]

        if num == ord(letter):
            player_points += 10
        else:
            player_points += 2

    if player_points >= winner_points:
        winner_name = player_name
        winner_points = player_points

print(f"The winner is {winner_name} with {winner_points} points!")
