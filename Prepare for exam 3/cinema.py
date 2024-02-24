# Read input
capacity = int(input())

total_income = 0
seats_left = capacity

while True:
    command = input()

    if command == "Movie time!":
        print(f"There are {seats_left} seats left in the cinema.")
        break

    people_entering = int(command)

    if people_entering > seats_left:
        print("The cinema is full.")
        break

    seats_left -= people_entering
    income = people_entering * 5

    if people_entering % 3 == 0:
        income -= 5

    total_income += income

print(f"Cinema income - {total_income} lv.")
