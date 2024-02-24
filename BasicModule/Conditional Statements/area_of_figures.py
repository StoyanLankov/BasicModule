from math import pi
# Read user input
figure = input()

area = 0

# Logic
if figure == 'square':
    a = float(input())
    area = a * a
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
elif figure == 'circle':
    a = float(input())
    area = pi * a * a
elif figure == 'triangle':
    a = float(input())
    c = float(input())
    area = (a * c) / 2
pass


# Print output
print(f'{area:.3f}')
