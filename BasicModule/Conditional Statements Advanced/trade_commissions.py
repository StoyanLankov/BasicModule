city = input()
trade = float(input())
commission = 0
is_input_valid = True

if city == 'Sofia':
    if 0 <= trade <= 500:
        commission = trade * 0.05
    elif 500 <= trade <= 1000:
        commission = trade * 0.07
    elif 1000 <= trade <= 10000:
        commission = trade * 0.08
    elif trade > 10000:
        commission = trade * 0.12
    else:
        is_input_valid = False

elif city == 'Varna':
    if 0 <= trade <= 500:
        commission = trade * 0.045
    elif 500 <= trade <= 1000:
        commission = trade * 0.075
    elif 1000 <= trade <= 10000:
        commission = trade * 0.10
    elif trade > 10000:
        commission = trade * 0.13
    else:
        is_input_valid = False

elif city == 'Plovdiv':
    if 0 <= trade <= 500:
        commission = trade * 0.055
    elif 500 <= trade <= 1000:
        commission = trade * 0.08
    elif 1000 <= trade <= 10000:
        commission = trade * 0.12
    elif trade > 10000:
        commission = trade * 0.145
    else:
        is_input_valid = False
else:
    is_input_valid = False

if is_input_valid:
    print(f'{commission:.2f}')
else:
    print('error')