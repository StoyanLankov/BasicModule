n = int(input())
l = int(input())

passwords = []

for digit1 in range(1, n + 1):
    for digit2 in range(1, n + 1):
        for letter1 in range(97, 97 + l):
            for letter2 in range(97, 97 + l):
                for digit3 in range(1, n + 1):
                    if digit3 > digit1 and digit3 > digit2:
                        password = f"{digit1}{digit2}{chr(letter1)}{chr(letter2)}{digit3}"
                        passwords.append(password)

print(" ".join(passwords))
