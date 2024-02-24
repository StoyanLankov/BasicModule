width = int(input())
length = int(input())
height = int(input())

total_volume = width * length * height
boxes_volume = 0

command = input()
while command != "Done":
    boxes_volume += int(command)
    if boxes_volume >= total_volume:
        break
    command = input()

if boxes_volume >= total_volume:
    space_needed = boxes_volume - total_volume
    print(f"No more free space! You need {space_needed} Cubic meters more.")
else:
    space_left = total_volume - boxes_volume
    print(f"{space_left} Cubic meters left.")
