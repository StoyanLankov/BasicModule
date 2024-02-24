amount_nylon_m2 = int(input())
amount_paint_l = int(input())
amount_thinner_l = int(input())
hours_workers = int(input())

price_nylon = 1.50
price_paint = 14.50
price_thinner = 5.00
bags = 0.40

extra_paint = (amount_paint_l * 1.1) * price_paint
extra_nylon = (amount_nylon_m2 + 2) * price_nylon
total_thinner = amount_thinner_l * price_thinner

sum = extra_nylon + extra_paint + total_thinner + bags

payment_workers = sum * (30 / 100)
final_sum = sum + payment_workers * hours_workers

print(final_sum)