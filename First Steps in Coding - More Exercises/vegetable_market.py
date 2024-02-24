price_kg_veg = float(input())
price_kg_fruit = float(input())
total_kg_veg = int(input())
total_kg_fruit = int(input())

sum_veg = price_kg_veg * total_kg_veg
sum_fruit = price_kg_fruit * total_kg_fruit
total = (sum_veg + sum_fruit) / 1.94
result = f'{total:.2f}'
print(result)