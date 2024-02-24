number_pack_pens = int(input())
number_pack_markers = int(input())
liquid_liter = int(input())
discount = int(input())

pens_price = 5.8 * number_pack_pens
markers_price = 7.2 * number_pack_markers
liquid_liter_price = 1.2 * liquid_liter

total_sum = pens_price + markers_price + liquid_liter_price
final_sum = total_sum - (total_sum * discount/100)
print(f'{final_sum:.2f}')

