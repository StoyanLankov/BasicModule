last_sector = input()
rows_first_sector = int(input())
seats_odd_row = int(input())

seats_count = 0

for sector in range(ord('A'), ord(last_sector) + 1):
    for row in range(1, rows_first_sector + 1):
        if row % 2 != 0:
            seats_in_row = seats_odd_row
        else:
            seats_in_row = seats_odd_row + 2

        for seat in range(0, seats_in_row):
            seat_letter = chr(ord('a') + seat)
            print(f"{chr(sector)}{row}{seat_letter}")
            seats_count += 1

print(seats_count)
