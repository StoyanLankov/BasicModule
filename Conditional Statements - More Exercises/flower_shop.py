import math

number_magnolia = int(input())
number_hyacinths = int(input())
number_rose = int(input())
number_cactus = int(input())
present_price = float(input())

magnolia_price = 3.25
hyacinths_price = 4
rose_price = 3.5
cactus_price = 8

final_price_for_magnolia = number_magnolia * magnolia_price
final_price_for_hyacinths = number_hyacinths * hyacinths_price
final_price_for_rose = number_rose * rose_price
final_price_for_cactus = number_cactus * cactus_price

total_price = final_price_for_cactus + final_price_for_rose + final_price_for_hyacinths + final_price_for_magnolia
taxes = total_price * 5/100
final_sum = total_price - taxes

difference = abs(present_price - final_sum)

if final_sum < present_price:
    print(f'She will have to borrow {(math.ceil(difference))} leva.')
else:
    print(f'She is left with {(math.floor(difference))} leva.')
