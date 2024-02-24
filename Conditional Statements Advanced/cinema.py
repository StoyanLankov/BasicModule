type_of_movie = input()
rows = int(input())
columns = int(input())
income = 0
total_seats = rows * columns

if type_of_movie == 'Premiere':
    income = total_seats * 12
elif type_of_movie == 'Normal':
    income = total_seats * 7.5
elif type_of_movie == 'Discount':
    income = total_seats * 5

print(f'{income:.2f} leva')