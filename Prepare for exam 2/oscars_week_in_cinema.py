movie_name = input()
type_hall = input()
number_of_tickets = int(input())

price_of_ticket = 0

if movie_name == 'A Star Is Born':
    if type_hall == 'normal':
        price_of_ticket += 7.5
    elif type_hall == 'luxury':
        price_of_ticket += 10.5
    elif type_hall == 'ultra luxury':
        price_of_ticket += 13.5
elif movie_name == 'Bohemian Rhapsody':
    if type_hall == 'normal':
        price_of_ticket += 7.35
    elif type_hall == 'luxury':
        price_of_ticket += 9.45
    elif type_hall == 'ultra luxury':
        price_of_ticket += 12.75
elif movie_name == 'Green Book':
    if type_hall == 'normal':
        price_of_ticket += 8.15
    elif type_hall == 'luxury':
        price_of_ticket += 10.25
    elif type_hall == 'ultra luxury':
        price_of_ticket += 13.25
elif movie_name == 'The Favourite':
    if type_hall == 'normal':
        price_of_ticket += 8.75
    elif type_hall == 'luxury':
        price_of_ticket += 11.55
    elif type_hall == 'ultra luxury':
        price_of_ticket += 13.95

total = price_of_ticket * number_of_tickets

print(f'{movie_name} -> {total:.2f} lv.')