goal = 10000
total_steps = 0

while total_steps < goal:
    input_data = input()
    if input_data == "Going home":
        steps_to_home = int(input())
        total_steps += steps_to_home
        difference = abs(total_steps - goal)
        if total_steps >= goal:
            print("Goal reached! Good job!")
            print(f"{difference} steps over the goal!")
        else:
            print(f"{difference} more steps to reach goal.")
        break
    else:
        steps = int(input_data)
        total_steps += steps

        if total_steps >= goal:
            difference = total_steps - goal
            print("Goal reached! Good job!")
            print(f"{difference} steps over the goal!")
            break
