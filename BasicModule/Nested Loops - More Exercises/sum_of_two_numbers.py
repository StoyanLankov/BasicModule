start = int(input())
end = int(input())
magic_number = int(input())

combination_count = 0
is_found = False

for num1 in range(start, end + 1):
    for num2 in range(start, end + 1):
        combination_count += 1
        if num1 + num2 == magic_number:
            print(f"Combination N:{combination_count} ({num1} + {num2} = {magic_number})")
            is_found = True
            break
    if is_found:
        break

if not is_found:
    print(f"{combination_count} combinations - neither equals {magic_number}")
