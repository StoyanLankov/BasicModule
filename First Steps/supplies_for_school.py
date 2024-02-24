pack_of_pens = int(input())
pack_of_markers = int(input())
cleaning_liquid = int(input())
discount = int(input())

pens = 5.80
markers = 7.20
liquid = 1.20
discount_ani = discount / 100

final_price_pens = pack_of_pens * pens
final_price_markers = pack_of_markers * markers
final_price_liquid = cleaning_liquid * liquid

total_price = final_price_pens + final_price_liquid + final_price_markers
final_price = total_price - (total_price * discount_ani)

print(final_price)