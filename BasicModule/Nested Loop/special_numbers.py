n = int(input())

for num in range(1111, 10000):
    is_special = True
    for digit in str(num):
        if digit == '0' or n % int(digit) != 0:
            is_special = False
            break
    if is_special:
        print(num, end=' ')
