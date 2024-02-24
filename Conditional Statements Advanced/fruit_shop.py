fruit = input()
day_of_week = input()
qty = float(input())
total = 0
is_input_correct = True

if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
    if fruit == 'banana':
        total = qty * 2.5
    elif fruit == 'apple':
        total = qty * 1.2
    elif fruit == 'orange':
        total = qty * 0.85
    elif fruit == 'grapefruit':
        total = qty * 1.45
    elif fruit == 'kiwi':
        total = qty * 2.7
    elif fruit == 'pineapple':
        total = qty * 5.5
    elif fruit == 'grapes':
        total = qty * 3.85
    else:
        is_input_correct = False
elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if fruit == 'banana':
        total = qty * 2.7
    elif fruit == 'apple':
        total = qty * 1.25
    elif fruit == 'orange':
        total = qty * 0.9
    elif fruit == 'grapefruit':
        total = qty * 1.6
    elif fruit == 'kiwi':
        total = qty * 3
    elif fruit == 'pineapple':
        total = qty * 5.6
    elif fruit == 'grapes':
        total = qty * 4.2
    else:
        is_input_correct = False
else:
    is_input_correct = False

if is_input_correct:
    print(f'{total:.2f}')
else:
    print('error')