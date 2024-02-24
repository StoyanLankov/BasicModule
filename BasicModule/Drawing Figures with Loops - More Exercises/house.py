n = int(input())

# Print the roof
roof_rows = (n + 1) // 2
if n % 2 == 0:
    stars = 2
else:
    stars = 1

for row in range(roof_rows):
    dashes = (n - stars) // 2
    print("-" * dashes + "*" * stars + "-" * dashes)
    stars += 2

# Print the base
base_rows = n // 2 - 1
for row in range(base_rows):
    print("|" + "*" * (n - 2) + "|")

# Print the bottom row
print("|" + "*" * (n - 2) + "|")
