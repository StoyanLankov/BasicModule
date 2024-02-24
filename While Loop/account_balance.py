total = 0

while True:
    command = input()

    if command == "NoMoreMoney":
        break

    amount = float(command)

    if amount < 0:
        print("Invalid operation!")
        break

    total += amount
    print(f"Increase: {amount:.2f}")

print(f"Total: {total:.2f}")
