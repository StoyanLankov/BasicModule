age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

saved_money = 0
toys_count = 0
money_gift = 10

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        saved_money += money_gift
        money_gift += 10
        saved_money -= 1
    else:
        toys_count += 1

total_money_from_toys = toys_count * toy_price
saved_money += total_money_from_toys

if saved_money >= washing_machine_price:
    remaining_money = saved_money - washing_machine_price
    print(f"Yes! {remaining_money:.2f}")
else:
    money_needed = washing_machine_price - saved_money
    print(f"No! {money_needed:.2f}")
