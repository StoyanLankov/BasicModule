number_chicken_menus = int(input())
number_fish_menus = int(input())
number_vegan_menus = int(input())

chicken_menu_price = 10.35 * number_chicken_menus
fish_menu_price = 12.40 * number_fish_menus
vegan_menu_price = 8.15 * number_vegan_menus

total_sum = chicken_menu_price + fish_menu_price + vegan_menu_price
dessert_price = total_sum * 0.2
delivery_fee = 2.5
final_sum = total_sum + dessert_price + delivery_fee
print(final_sum)
