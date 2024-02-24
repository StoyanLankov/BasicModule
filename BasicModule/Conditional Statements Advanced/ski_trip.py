days = int(input())
type_of_room = input()
rate = input()
nights = days - 1
total_price = 0

if type_of_room == 'room for one person':
    total_price = 18
elif type_of_room == 'apartment':
    total_price = 25
    if nights < 10:
        total_price *= 0.7
    elif nights < 15:
        total_price *= 0.65
    elif nights > 15:
        total_price *= 0.5
elif type_of_room == 'president apartment':
    total_price = 35
    if nights < 10:
        total_price *= 0.9
    elif nights < 15:
        total_price *= 0.85
    elif nights > 15:
        total_price *= 0.8

total_sum = nights * total_price

if rate == 'positive':
    total_sum *= 1.25
elif rate == 'negative':
    total_sum *= 0.90

print(f'{total_sum:.2f}')