coins_1lv = int(input())
coins_2lv = int(input())
banknotes_5lv = int(input())
target_sum = int(input())

combinations_count = 0

for i in range(coins_1lv + 1):
    for j in range(coins_2lv + 1):
        for k in range(banknotes_5lv + 1):
            current_sum = i * 1 + j * 2 + k * 5
            if current_sum == target_sum:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {target_sum} lv.")
                combinations_count += 1

if combinations_count == 0:
    print("No valid combinations.")
