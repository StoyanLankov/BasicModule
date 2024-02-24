peter_budget = float(input())
number_gpu = int(input())
number_cpu = int(input())
number_ram_memory = int(input())

price_gpu = number_gpu * 250
price_cpu = price_gpu * 0.35
price_ram = price_gpu * 0.10

total_sum_cpu = number_cpu * price_cpu
total_sum_ram = number_ram_memory * price_ram

total_sum_all = price_gpu + total_sum_cpu + total_sum_ram

if number_gpu > number_cpu:
    total_sum_all *= 0.85

difference = abs(total_sum_all - peter_budget)

if peter_budget >= total_sum_all:
    print(f'You have {difference:.2f} leva left!')

else:
    print(f'Not enough money! You need {difference:.2f} leva more!')
