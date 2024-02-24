deposit = float(input())
term = int(input())
apy = float(input())

total_apy = deposit * apy / 100
yield_per_month = total_apy / 12
total_sum = deposit + term * yield_per_month
print(total_sum)
