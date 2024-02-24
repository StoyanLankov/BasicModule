time_for_shoots = int(input())
number_of_scene = int(input())
time_of_scene = int(input())

prepare_for_area = time_for_shoots * 0.15
time_for_shoot_scene = prepare_for_area + (number_of_scene * time_of_scene)


if time_for_shoot_scene <= time_for_shoots:
    remaining_time = round(time_for_shoots - time_for_shoot_scene)
    print(f"You managed to finish the movie on time! You have {remaining_time} minutes left!")
else:
    needed_time = round(time_for_shoot_scene - time_for_shoots)
    print(f"Time is up! To complete the movie you need {needed_time} minutes.")