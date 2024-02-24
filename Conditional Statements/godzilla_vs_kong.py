budget_for_movie = float(input())
number_people = int(input())
price_dress_people = float(input())

background_budget = budget_for_movie * 0.10

if number_people > 150:
    sum_dress = number_people * price_dress_people
    sum_dress *= 0.90
else:
    sum_dress = number_people * price_dress_people

total_sum_movie = background_budget + sum_dress
left_money = abs(total_sum_movie - budget_for_movie)


if total_sum_movie > budget_for_movie:
    print('Not enough money!')
    print(f'Wingard needs {left_money:.2f} leva more.')

else:
    print(f'Action!')
    print(f'Wingard starts filming with {left_money:.2f} leva left.')


