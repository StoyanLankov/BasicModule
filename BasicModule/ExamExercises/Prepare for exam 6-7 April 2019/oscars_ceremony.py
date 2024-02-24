rent_hall = int(input())

statue = rent_hall * 0.7
catering = statue * 0.85
sound = catering / 2

total = rent_hall + statue + catering + sound
print(f'{total:.2f}')