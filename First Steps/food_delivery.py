amount_chicken_menu = int(input())
amount_fish_menu = int(input())
amount_veggie_menu = int(input())

chicken_menu = 10.35
fish_menu = 12.40
veggie_menu = 8.15
delivery_fee = 2.50

final_price_chicken = amount_chicken_menu * chicken_menu
final_price_fish = amount_fish_menu * fish_menu
final_price_veggie = amount_veggie_menu * veggie_menu

total_sum = final_price_veggie + final_price_fish + final_price_chicken

desert_price = total_sum * (20 / 100)

final_sum = total_sum + desert_price + delivery_fee

print(f'{final_sum:.2f}')