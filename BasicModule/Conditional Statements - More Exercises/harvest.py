import math

x = int(input())
y = float(input())
z = int(input())
number_workers = int(input())

total_grapes = x * y
vine = math.ceil(0.40 * total_grapes / 2.5)
left_litters_vine = abs(vine - z)
left_for_workers = math.ceil(left_litters_vine / number_workers)


if vine < z:
    print(f'It will be a tough winter! More {left_litters_vine} liters wine needed.')
else:
    print (f'Good harvest this year! Total wine: {vine} liters.')
    print (f'{left_litters_vine} liters left -> {left_for_workers} liters per person.')