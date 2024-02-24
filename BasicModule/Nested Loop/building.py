floors = int(input())
rooms_per_floor = int(input())

for floor in range(floors, 0, -1):
    room_type = ""
    if floor % 2 == 0:
        room_type = "O"
    else:
        room_type = "A"

    if floor == floors:
        room_type = "L"

    for room in range(rooms_per_floor):
        room_number = str(floor) + str(room)
        print(f"{room_type}{room_number}", end=" ")
    print()
