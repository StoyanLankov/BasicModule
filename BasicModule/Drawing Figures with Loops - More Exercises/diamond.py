n = int(input())

# Print the upper half of the diamond
left_right = (n - 1) // 2

for row in range(left_right + 1):
    dashes = left_right - row
    stars = n - 2 * dashes

    if stars > 1:
        middle = stars - 2
        print("-" * dashes + "*" + "-" * middle + "*" + "-" * dashes)
    else:
        print("-" * dashes + "*" + "-" * dashes)

# Print the lower half of the diamond
for row in range(left_right):
    dashes = row + 1
    stars = n - 2 * dashes

    if stars > 1:
        middle = stars - 2
        print("-" * dashes + "*" + "-" * middle + "*" + "-" * dashes)
    else:
        print("-" * dashes + "*" + "-" * dashes)
