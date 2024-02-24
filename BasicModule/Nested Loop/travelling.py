destination = input()
total_budget = 0

while destination != "End":
    min_budget = float(input())
    saved_money = 0

    while saved_money < min_budget:
        money = float(input())
        saved_money += money

    print(f"Going to {destination}!")
    destination = input()

