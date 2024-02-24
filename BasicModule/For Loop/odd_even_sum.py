n = int(input())

even_sum = 0
odd_sum = 0

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

if odd_sum == even_sum:
    print(f'Yes')
    print(f'Sum = {odd_sum}')
else:
    diff = abs(even_sum - odd_sum)
    print(f'No')
    print(f'Diff = {diff}')