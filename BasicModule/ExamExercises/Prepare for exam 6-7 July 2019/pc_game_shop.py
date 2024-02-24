total_games = int(input())
hearthstone_count = 0
fortnite_count = 0
overwatch_count = 0
others_count = 0

for _ in range(total_games):
    game_name = input()

    if game_name == "Hearthstone":
        hearthstone_count += 1
    elif game_name == "Fornite":
        fortnite_count += 1
    elif game_name == "Overwatch":
        overwatch_count += 1
    else:
        others_count += 1

hearthstone_percentage = (hearthstone_count / total_games) * 100
fortnite_percentage = (fortnite_count / total_games) * 100
overwatch_percentage = (overwatch_count / total_games) * 100
others_percentage = (others_count / total_games) * 100

print(f"Hearthstone - {hearthstone_percentage:.2f}%")
print(f"Fornite - {fortnite_percentage:.2f}%")
print(f"Overwatch - {overwatch_percentage:.2f}%")
print(f"Others - {others_percentage:.2f}%")
