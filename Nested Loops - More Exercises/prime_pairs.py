def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

start_first_pair = int(input())
start_second_pair = int(input())
diff_first_pair = int(input())
diff_second_pair = int(input())

end_first_pair = start_first_pair + diff_first_pair
end_second_pair = start_second_pair + diff_second_pair

for i in range(start_first_pair, end_first_pair + 1):
    for j in range(start_second_pair, end_second_pair + 1):
        if is_prime(i) and is_prime(j):
            print(f"{i}{j}")
