total_cargo = int(input())
microbus_cargo = 0
truck_cargo = 0
train_cargo = 0
total_weight = 0

for _ in range(total_cargo):
    cargo = int(input())
    total_weight += cargo

    if cargo <= 3:
        microbus_cargo += cargo
    elif cargo >= 4 and cargo <= 11:
        truck_cargo += cargo
    elif cargo >= 12:
        train_cargo += cargo

average_price = (microbus_cargo * 200 + truck_cargo * 175 + train_cargo * 120) / total_weight
microbus_percentage = (microbus_cargo / total_weight) * 100
truck_percentage = (truck_cargo / total_weight) * 100
train_percentage = (train_cargo / total_weight) * 100

print(f"{average_price:.2f}")
print(f"{microbus_percentage:.2f}%")
print(f"{truck_percentage:.2f}%")
print(f"{train_percentage:.2f}%")
