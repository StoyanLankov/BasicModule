fuel_type = input()
fuel_level = float(input())

if fuel_type == "Diesel":
    if fuel_level >= 25:
        print("You have enough Diesel.")
    else:
        print("Fill your tank with Diesel!")
elif fuel_type == "Gasoline":
    if fuel_level >= 25:
        print("You have enough Gasoline.")
    else:
        print("Fill your tank with Gasoline!")
elif fuel_type == "Gas":
    if fuel_level >= 25:
        print("You have enough Gas.")
    else:
        print("Fill your tank with Gas!")
else:
    print("Invalid fuel!")
