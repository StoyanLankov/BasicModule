width = float(input())
length = float(input())

width_hall = length * 100 - 100
total_desks = width_hall // 70
length_hall = width * 100
number_row = length_hall // 120

counts_places = total_desks * number_row - 3
print(int(counts_places))