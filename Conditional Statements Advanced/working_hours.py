time_of_day = int(input())
day_of_week = input()

if not day_of_week == 'Sunday' and 10 <= time_of_day <= 18:
    print('open')
else:
    print('closed')
