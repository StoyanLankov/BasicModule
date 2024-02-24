detergent_quantity = int(input()) * 750
dishes_count = 0
pots_count = 0
detergent_needed = 0

counter = 0
command = input()

while command != "End":
    counter += 1
    quantity = int(command)
    if counter % 3 == 0:
        pots_count += quantity
        detergent_needed += quantity * 15
    else:
        dishes_count += quantity
        detergent_needed += quantity * 5

    if detergent_needed > detergent_quantity:
        print(f"Not enough detergent, {detergent_needed - detergent_quantity} ml. more necessary!")
        exit()

    command = input()

print("Detergent was enough!")
print(f"{dishes_count} dishes and {pots_count} pots were washed.")
print(f"Leftover detergent {detergent_quantity - detergent_needed} ml.")
