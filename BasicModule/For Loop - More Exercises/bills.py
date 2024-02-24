months = int(input())
water = 20
internet = 15
total_bill = 0
total_others = 0
total_avg = 0
for i in range(1, months + 1):
    bill = float(input())
    total_bill += bill
    others = (water + internet + bill) * 1.20
    total_others += others
    avg = (water + internet + others + bill) / months
    total_avg += avg
print(f"Electricity: {total_bill:.2f} lv")
print(f"Water: {months * water:.2f} lv")
print(f"Internet: {months * internet:.2f} lv")
print(f"Other: {total_others:.2f} lv")
print(f"Average: {total_avg:.2f} lv")