n = int(input())

print("*" * (2*n) + " " * n + "*" * (2*n))

middle_rows = n - 2
if middle_rows % 2 == 1:
    middle_row = middle_rows // 2
else:
    middle_row = middle_rows // 2 - 1

for i in range(middle_rows):
    if i == middle_row:
        print("*" + "/" * (2*n-2) + "*" + "|" * n + "*" + "/" * (2*n-2) + "*")
    else:
        print("*" + "/" * (2*n-2) + "*" + " " * n + "*" + "/" * (2*n-2) + "*")

print("*" * (2*n) + " " * n + "*" * (2*n))
