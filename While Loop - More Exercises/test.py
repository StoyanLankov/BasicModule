minutes = int(input())
seconds = int(input())
slope_length = float(input())
time_per_100m = int(input())

total_control_time = minutes * 60 + seconds
time_reduction = (slope_length / 120) * 2.5
marin_time = (slope_length / 100) * time_per_100m - time_reduction

if marin_time <= total_control_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {marin_time:.3f}.")
else:
    difference = marin_time - total_control_time
    print(f"No, Marin failed! He was {difference:.3f} second slower.")
