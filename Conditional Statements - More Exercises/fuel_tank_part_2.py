fuel_type = input()
fuel_quantity = float(input())
has_discount_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

discount_gasoline = 0.18
discount_diesel = 0.12
discount_gas = 0.08

discount_range_low = 20
discount_range_high = 25
discount_range_low_percent = 0.08
discount_range_high_percent = 0.10

if fuel_type == "Gasoline":
    fuel_price = gasoline_price
    if has_discount_card == "Yes":
        fuel_price -= discount_gasoline
elif fuel_type == "Diesel":
    fuel_price = diesel_price
    if has_discount_card == "Yes":
        fuel_price -= discount_diesel
elif fuel_type == "Gas":
    fuel_price = gas_price
    if has_discount_card == "Yes":
        fuel_price -= discount_gas
else:
    print("Invalid fuel type!")
    exit()

total_price = fuel_price * fuel_quantity

if discount_range_low <= fuel_quantity <= discount_range_high:
    total_price -= total_price * discount_range_low_percent
elif fuel_quantity > discount_range_high:
    total_price -= total_price * discount_range_high_percent

print(f"{total_price:.2f} lv.")
