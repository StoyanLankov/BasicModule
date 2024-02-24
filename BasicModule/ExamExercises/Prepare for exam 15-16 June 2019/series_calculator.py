series_name = input()
seasons = int(input())
episodes_per_season = int(input())
episode_duration = float(input())

commercial_duration = episode_duration * 0.2
episode_duration_with_commercials = episode_duration + commercial_duration
special_episode_duration = episode_duration_with_commercials + 10

total_time = seasons * episodes_per_season * episode_duration_with_commercials + (seasons * 10)

print(f"Total time needed to watch the {series_name} series is {int(total_time)} minutes.")
