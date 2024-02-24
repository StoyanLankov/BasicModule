# Read user input
degree = float(input())

# Logic
if degree > 35:
    print('unknown')
elif degree >= 26:
    print('Hot')
elif degree >= 20.1:
    print('Warm')
elif degree >= 15:
    print('Mild')
elif degree >= 12:
    print('Cool')
elif degree >= 5:
    print('Cold')
else:
    print('unknown')