actor_name = input()
academy_points = float(input())
evaluators_count = int(input())

total_points = academy_points

for i in range(evaluators_count):
    evaluator_name = input()
    evaluator_points = float(input())

    points = len(evaluator_name) * evaluator_points / 2
    total_points += points

    if total_points >= 1250.5:
        break

if total_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    needed_points = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
