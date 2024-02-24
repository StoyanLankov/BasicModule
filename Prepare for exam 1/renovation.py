import math

wall_height = int(input())
wall_width = int(input())
unpainted_percentage = int(input())

total_area = 4 * (wall_height * wall_width)
painted_area = math.ceil(total_area - (total_area * unpainted_percentage / 100))

command = input()
paint_left = 0

while command != "Tired!":
    paint_liters = int(command)
    painted_area -= paint_liters

    if painted_area <= 0:
        paint_left = abs(painted_area)
        break

    command = input()

if painted_area > 0:
    print(f"{painted_area} quadratic m left.")
elif paint_left > 0:
    print(f"All walls are painted and you have {paint_left} l paint left!")
else:
    print("All walls are painted! Great job, Pesho!")
