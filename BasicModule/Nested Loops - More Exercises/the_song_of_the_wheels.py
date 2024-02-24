M = int(input())

found_password = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
              

                    print(f"{a}{b}{c}{d}", end=" ")
                    found_password = True
1
if found_password:
    print()
    print(f"Password: {a}{b}{c}{d}")
else:
    print("No!")
