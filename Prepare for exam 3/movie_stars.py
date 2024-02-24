# Read input
budget = float(input())

while True:
    actor_info = input()

    if actor_info == "ACTION":
        break

    actor_name = actor_info

    if len(actor_name) > 15:
        payment = budget * 0.2
    else:
        payment = float(input())

    budget -= payment

    if budget < 0:
        needed_budget = abs(budget)
        print(f"We need {needed_budget:.2f} leva for our actors.")
        break

if budget >= 0:
    print(f"We are left with {budget:.2f} leva.")
