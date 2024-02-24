n = int(input())
salary = int(input())

total_penalty = 0

for i in range(n):
    website = input()

    if website == "Facebook":
        total_penalty += 150
    elif website == "Instagram":
        total_penalty += 100
    elif website == "Reddit":
        total_penalty += 50

    if salary <= total_penalty:
        print("You have lost your salary.")
        exit(0)

remaining_salary = salary - total_penalty
print(remaining_salary)
