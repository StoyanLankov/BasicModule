movie_name = input()
number_day = int(input())
number_tickets = int(input())
price_ticket = float(input())
percentage_for_cinema = int(input())

price_for_day = number_tickets * price_ticket
total = number_day * price_for_day
percentage = total * percentage_for_cinema / 100
final = total - percentage
print(f'The profit from the movie {movie_name} is {final:.2f} lv.')