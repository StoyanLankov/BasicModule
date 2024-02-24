n = int(input())

odd_sum = 0
odd_min = float('inf')
odd_max = float('-inf')

even_sum = 0
even_min = float('inf')
even_max = float('-inf')

for i in range(1, n + 1):
    num = float(input())

    if i % 2 == 0:
        even_sum += num
        if num > even_max:
            even_max = num
        if num < even_min:
            even_min = num
    else:
        odd_sum += num
        if num > odd_max:
            odd_max = num
        if num < odd_min:
            odd_min = num

print(f"OddSum={odd_sum:.2f},\n", end="")
if odd_min != float('inf'):
    print(f"OddMin={odd_min:.2f},\n", end="")
else:
    print("OddMin=No,\n", end="")
if odd_max != float('-inf'):
    print(f"OddMax={odd_max:.2f},\n", end="")
else:
    print("OddMax=No,\n", end="")

print(f"EvenSum={even_sum:.2f},\n", end="")
if even_min != float('inf'):
    print(f"EvenMin={even_min:.2f},\n", end="")
else:
    print("EvenMin=No,\n", end="")
if even_max != float('-inf'):
    print(f"EvenMax={even_max:.2f}")
else:
    print("EvenMax=No")
