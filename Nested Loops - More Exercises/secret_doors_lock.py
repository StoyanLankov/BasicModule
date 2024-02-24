upper_limit_hundreds = int(input())
upper_limit_tens = int(input())
upper_limit_ones = int(input())

for hundreds in range(2, upper_limit_hundreds + 1, 2):
    for tens in [2, 3, 5, 7]:
        if tens <= upper_limit_tens:
            for ones in range(2, upper_limit_ones + 1, 2):
                print(f"{hundreds} {tens} {ones}")
