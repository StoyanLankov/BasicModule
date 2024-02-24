start_letter = input()
end_letter = input()
skip_letter = input()

count = 0

for letter1 in range(ord(start_letter), ord(end_letter) + 1):
    for letter2 in range(ord(start_letter), ord(end_letter) + 1):
        for letter3 in range(ord(start_letter), ord(end_letter) + 1):
            combination = chr(letter1) + chr(letter2) + chr(letter3)
            if skip_letter not in combination:
                print(combination, end=" ")
                count += 1

print(count)
