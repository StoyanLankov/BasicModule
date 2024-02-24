total_student_tickets = 0
total_standard_tickets = 0
total_kid_tickets = 0
total_tickets = 0

while True:
    movie = input()
    if movie == "Finish":
        break

    seats = int(input())
    sold_tickets = 0

    while sold_tickets < seats:
        ticket_type = input()

        if ticket_type == "End":
            break

        sold_tickets += 1
        total_tickets += 1

        if ticket_type == "student":
            total_student_tickets += 1
        elif ticket_type == "standard":
            total_standard_tickets += 1
        elif ticket_type == "kid":
            total_kid_tickets += 1

    percent_full = (sold_tickets / seats) * 100
    print(f"{movie} - {percent_full:.2f}% full.")

total_percentage_student = (total_student_tickets / total_tickets) * 100
total_percentage_standard = (total_standard_tickets / total_tickets) * 100
total_percentage_kid = (total_kid_tickets / total_tickets) * 100

print(f"Total tickets: {total_tickets}")
print(f"{total_percentage_student:.2f}% student tickets.")
print(f"{total_percentage_standard:.2f}% standard tickets.")
print(f"{total_percentage_kid:.2f}% kids tickets.")
