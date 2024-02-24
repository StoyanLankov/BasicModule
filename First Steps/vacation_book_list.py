page_numbers = int(input())
pages_per_hour = int(input())
days = int(input())

read_hours = page_numbers / pages_per_hour
needed_hours = read_hours / days

print(round(needed_hours))

