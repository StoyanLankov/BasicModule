from math import ceil

name_serial = str(input())
length_serial = int(input())
length_rest = int(input())

time_for_lunch = length_rest * 1/8
time_for_air = length_rest * 1/4
left_time = length_rest - time_for_lunch - time_for_air
difference = ceil(abs(left_time - length_serial))

if left_time >= length_serial:
    print(f'You have enough time to watch {name_serial} and left with {difference} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_serial}, you need {difference} more minutes.")