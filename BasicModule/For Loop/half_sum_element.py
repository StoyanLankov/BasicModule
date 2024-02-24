import sys
n = int(input())
sum = 0
max_element = -sys.maxsize
for i in range(n):
    current_element = int(input())
    sum += current_element
    if current_element > max_element:
        max_element = current_element
if max_element == sum - max_element:
    print(f'Yes')
    print(f'Sum = {max_element}')
else:
    diff = abs(max_element - (sum - max_element))
    print(f'No')
    print(f'Diff = {diff}')
