a = int(input())
b = int(input())
max_combinations = int(input())

combinations_count = 0

for i in range(1, a + 1):
    for j in range(1, b + 1):
        if combinations_count == max_combinations:
            break

        char_A = chr(35 + (i % 21))
        char_B = chr(64 + (j % 33))
        char_x = str(i)
        char_y = str(j)

        password = f"{char_A}{char_B}{char_x}{char_y}{char_B}{char_A}"
        print(password, end="|")

        combinations_count += 1

    if combinations_count == max_combinations:
        break

print()
