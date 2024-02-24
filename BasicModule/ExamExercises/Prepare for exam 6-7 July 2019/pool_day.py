from math import ceil

amount_people = int(input())
entry_fee = float(input())
price_per_sunbed = float(input())
price_per_umbrella = float(input())

sum_for_entry_fee = amount_people * entry_fee
sunbed_needed = ceil(amount_people * 0.75)
umbrella_needed = ceil(amount_people * 0.5)

total_sunbed = sunbed_needed * price_per_sunbed
total_umbrella = umbrella_needed * price_per_umbrella

total_sum = sum_for_entry_fee + total_sunbed + total_umbrella

print(f'{total_sum:.2f} lv.')
