juniors_count = int(input())
seniors_count = int(input())
track_type = input()

juniors_fee = 0
seniors_fee = 0

if track_type == "trail":
    juniors_fee = 5.50
    seniors_fee = 7
elif track_type == "cross-country":
    juniors_fee = 8
    seniors_fee = 9.50
elif track_type == "downhill":
    juniors_fee = 12.25
    seniors_fee = 13.75
elif track_type == "road":
    juniors_fee = 20
    seniors_fee = 21.50

total_participants = juniors_count + seniors_count
total_fee = (juniors_count * juniors_fee) + (seniors_count * seniors_fee)

if total_participants >= 50 and track_type == "cross-country":
    total_fee *= 0.75

total_fee -= total_fee * 0.05

print(f"{total_fee:.2f}")
