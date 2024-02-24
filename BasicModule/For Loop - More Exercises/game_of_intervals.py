turns = int(input())

points = 0
from_0_to_9_count = 0
from_10_to_19_count = 0
from_20_to_29_count = 0
from_30_to_39_count = 0
from_40_to_50_count = 0
invalid_numbers_count = 0

for _ in range(turns):
    number = int(input())

    if 0 <= number <= 9:
        points += number * 0.2
        from_0_to_9_count += 1
    elif 10 <= number <= 19:
        points += number * 0.3
        from_10_to_19_count += 1
    elif 20 <= number <= 29:
        points += number * 0.4
        from_20_to_29_count += 1
    elif 30 <= number <= 39:
        points += 50
        from_30_to_39_count += 1
    elif 40 <= number <= 50:
        points += 100
        from_40_to_50_count += 1
    else:
        points /= 2
        invalid_numbers_count += 1

total_count = from_0_to_9_count + from_10_to_19_count + from_20_to_29_count + from_30_to_39_count + from_40_to_50_count + invalid_numbers_count

print(f"{points:.2f}")
print(f"From 0 to 9: {(from_0_to_9_count / total_count * 100):.2f}%")
print(f"From 10 to 19: {(from_10_to_19_count / total_count * 100):.2f}%")
print(f"From 20 to 29: {(from_20_to_29_count / total_count * 100):.2f}%")
print(f"From 30 to 39: {(from_30_to_39_count / total_count * 100):.2f}%")
print(f"From 40 to 50: {(from_40_to_50_count / total_count * 100):.2f}%")
print(f"Invalid numbers: {(invalid_numbers_count / total_count * 100):.2f}%")
