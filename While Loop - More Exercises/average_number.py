n = int(input())

sum_numbers = 0

for _ in range(n):
    number = int(input())
    sum_numbers += number

average = sum_numbers / n
print(f'{average:.2f}')
