voucher = int(input())
total_tickets = 0
other_purchases = 0

while True:
    purchase = input()
    if purchase == "End":
        break

    price = 0

    if len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
    else:
        price = ord(purchase[0])

    if price > voucher:
        break

    if len(purchase) > 8:
        total_tickets += 1
    else:
        other_purchases += 1

    voucher -= price

print(total_tickets)
print(other_purchases)
