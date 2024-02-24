capacity_stadium = int(input())
numbers_all_fans = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for i in range(1, numbers_all_fans + 1):
    sector = input()
    if sector == 'A':
        sector_a += 1
    elif sector == 'B':
        sector_b += 1
    elif sector == 'V':
        sector_v += 1
    elif sector == 'G':
        sector_g += 1

sector_a_percentage = sector_a / numbers_all_fans
sector_b_percentage = sector_b / numbers_all_fans
sector_v_percentage = sector_v / numbers_all_fans
sector_g_percentage = sector_g / numbers_all_fans
total_fans_percentage = numbers_all_fans / capacity_stadium

print("{:.2%}".format(sector_a_percentage))
print("{:.2%}".format(sector_b_percentage))
print("{:.2%}".format(sector_v_percentage))
print("{:.2%}".format(sector_g_percentage))
print("{:.2%}".format(total_fans_percentage))