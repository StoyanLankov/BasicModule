number_days_off = int(input())

tom_playing_time = 30000
working_days = 365 - number_days_off
playing_time = (working_days * 63) + (number_days_off * 127)
difference = abs(tom_playing_time - playing_time)

hours = difference // 60
minutes = difference % 60


if tom_playing_time <= playing_time:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')