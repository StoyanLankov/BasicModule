first_number = int(input())
second_number = int(input())

found_numbers = []

for num in range(first_number, second_number + 1):
    digits = [int(digit) for digit in str(num)]
    even_sum = sum(digits[::2])
    odd_sum = sum(digits[1::2])
    if even_sum == odd_sum:
        found_numbers.append(num)

if found_numbers:
    print(' '.join(str(num) for num in found_numbers))
