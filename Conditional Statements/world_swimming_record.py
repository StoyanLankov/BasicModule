from math import floor

record_seconds = float(input())
distance_meters = float(input())
time_in_sec_for_1m = float(input())

time_for_full_distance = distance_meters * time_in_sec_for_1m
resistance_water = floor(distance_meters / 15)
time_for_15_meters = resistance_water * 12.5
total_time = time_for_15_meters + time_for_full_distance

left_time = abs(total_time - record_seconds)

if total_time >= record_seconds:
    print(f'No, he failed! He was {left_time:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')