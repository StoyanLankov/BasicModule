total_nylon_m2 = int(input())
total_paint_liter = int(input())
total_thinner_liter = int(input())
working_hours = int(input())

nylon_price = (total_nylon_m2 + 2) * 1.5
paint_price = (total_paint_liter * 1.1) * 14.5
thinner_price = total_thinner_liter * 5
bags = 0.4

total_sum_materials = nylon_price + paint_price + thinner_price + bags
workers_wage = (total_sum_materials * 30/100) * working_hours
final_sum = total_sum_materials + workers_wage

print(f'{final_sum:.2f}')
