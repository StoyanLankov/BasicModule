area = float(input())
price_before_discount = area * 7.61
discount = price_before_discount * 0.18
price_after_discount = price_before_discount - discount

print(f'The final price is: {price_after_discount} lv.')
print(f'The discount is {discount} lv.')