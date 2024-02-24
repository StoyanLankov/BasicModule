months = input()
nights = int(input())

studio_price = 0
apartment_price = 0

if months == 'May' or months == 'October':
    studio_price = 50 * nights
    apartment_price = 65 * nights
    if nights > 14:
        studio_price -= studio_price * 0.3
        apartment_price -= apartment_price * 0.1
    elif nights > 7:
        studio_price -= studio_price * 0.05
elif months == 'June' or months == 'September':
    studio_price = 75.2 * nights
    apartment_price = 68.7 * nights
    if nights > 14:
        studio_price -= studio_price * 0.2
        apartment_price -= apartment_price * 0.1
elif months == 'July' or months == 'August':
    studio_price = 76 * nights
    apartment_price = 77 * nights
    if nights > 14:
        apartment_price -= apartment_price * 0.1

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')