start = int(input())
end = int(input())

special_numbers = []

for first in range(start, end + 1):
    for second in range(start, end + 1):
        for third in range(start, end + 1):
            for fourth in range(start, end + 1):
                if (first % 2 == 0 and fourth % 2 == 1) or (first % 2 == 1 and fourth % 2 == 0):
                    if first > fourth and (second + third) % 2 == 0:
                        special_numbers.append(f"{first}{second}{third}{fourth}")

print(" ".join(special_numbers))
