budget = float(input())
seasons = input()
destination = ''
type_of_holiday = ''

if budget <= 100:
    destination = 'Bulgaria'
    if seasons == 'summer':
        budget *= 0.3
        type_of_holiday = 'Camp'
    elif seasons == 'winter':
        budget *= 0.7
        type_of_holiday = 'Hotel'

elif budget <= 1000:
    destination = 'Balkans'
    if seasons == 'summer':
        budget *= 0.4
        type_of_holiday = 'Camp'
    elif seasons == 'winter':
        budget *= 0.8
        type_of_holiday = 'Hotel'

else:
    destination = 'Europe'
    type_of_holiday = 'Hotel'
    budget *= 0.90

print(f'Somewhere in {destination}')
print(f'{type_of_holiday} - {budget:.2f}')
