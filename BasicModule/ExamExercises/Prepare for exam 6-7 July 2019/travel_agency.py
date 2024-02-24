city = input()
package = input()
vip_discount = input()
days = int(input())

price_per_day = 0

if city == "Bansko" or city == "Borovets":
    if package == "noEquipment":
        price_per_day = 80
        if vip_discount == "yes":
            price_per_day *= 0.95
    elif package == "withEquipment":
        price_per_day = 100
        if vip_discount == "yes":
            price_per_day *= 0.90

elif city == "Varna" or city == "Burgas":
    if package == "noBreakfast":
        price_per_day = 100
        if vip_discount == "yes":
            price_per_day *= 0.93
    elif package == "withBreakfast":
        price_per_day = 130
        if vip_discount == "yes":
            price_per_day *= 0.88

total_price = price_per_day * days

if days > 7:
    total_price -= price_per_day

if city in ["Bansko", "Borovets", "Varna", "Burgas"] and package in ["noEquipment", "withEquipment", "noBreakfast", "withBreakfast"]:
    if days >= 1:
        print(f"The price is {total_price:.2f}lv! Have a nice time!")
    else:
        print("Days must be positive number!")
else:
    print("Invalid input!")