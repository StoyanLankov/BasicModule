cake_width = int(input())
cake_length = int(input())

cake_size = cake_width * cake_length
taken_pieces = 0
command = input()

while command != "STOP":
    pieces_taken = int(command)
    taken_pieces += pieces_taken

    if taken_pieces >= cake_size:
        break

    command = input()

if taken_pieces < cake_size:
    pieces_left = cake_size - taken_pieces
    print(f"{pieces_left} pieces are left.")
else:
    pieces_needed = taken_pieces - cake_size
    print(f"No more cake left! You need {pieces_needed} pieces more.")
