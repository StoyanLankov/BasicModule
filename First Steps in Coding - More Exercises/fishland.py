mackerel = float(input())
sprinkle = float(input())
bonito = float(input())
safrid = float(input())
mussels = int(input())

bonito_price = mackerel + (mackerel * 0.60)
safrid_price = sprinkle + (sprinkle * 0.8)
mussels_price = mussels * 7.5

total = (bonito_price * bonito) + (safrid_price * safrid) + mussels_price
print(f'{total:.2f}')
