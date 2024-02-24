N = int(input())

found_numbers = []

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                if i + j == k + l and N % (i + j) == 0:
                    found_numbers.append(f"{i}{j}{k}{l}")

print(" ".join(found_numbers))
