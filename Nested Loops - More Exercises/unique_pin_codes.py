first_digit_limit = int(input())
second_digit_limit = int(input())
third_digit_limit = int(input())

for first_digit in range(2, first_digit_limit + 1, 2):
    for second_digit in range(2, second_digit_limit + 1):
        if second_digit in [2, 3, 5, 7]:
            for third_digit in range(2, third_digit_limit + 1, 2):
                print(f"{first_digit} {second_digit} {third_digit}")
