unsatisfactory_grades = int(input())
problem_count = 0
total_score = 0
last_problem = ""
unsatisfactory_count = 0

while True:
    problem_name = input()
    if problem_name == "Enough":
        break
    grade = int(input())
    problem_count += 1
    total_score += grade
    last_problem = problem_name

    if grade <= 4:
        unsatisfactory_count += 1
        if unsatisfactory_count == unsatisfactory_grades:
            break

if problem_name == "Enough":
    average_score = total_score / problem_count
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {problem_count}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {unsatisfactory_count} poor grades.")
