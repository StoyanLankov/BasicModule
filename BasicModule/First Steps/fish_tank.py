length_cm = int(input())
width_cm = int(input())
high_cm = int(input())
percent = float(input())

area = length_cm * width_cm * high_cm
area_litter = area / 1000
percent_area = area_litter * (1 - percent / 100)

print(percent_area)