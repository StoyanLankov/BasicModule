annual_fee = int(input())

shoes = annual_fee - (annual_fee * 40/100)
uniform = shoes - (shoes * 20/100)
basketball_ball = 1/4 * uniform
accessories = 1/5 * basketball_ball

total_price = annual_fee + shoes + uniform + basketball_ball + accessories
print(total_price)
