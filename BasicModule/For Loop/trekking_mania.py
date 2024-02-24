number_of_groups = int(input())

mousala_count = 0
monblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

for i in range(number_of_groups):
    num_of_people = int(input())
    if num_of_people <= 5:
        mousala_count += num_of_people
    elif num_of_people <= 12:
        monblan_count += num_of_people
    elif num_of_people <= 25:
        kilimanjaro_count += num_of_people
    elif num_of_people <= 40:
        k2_count += num_of_people
    else:
        everest_count += num_of_people

total = mousala_count + monblan_count + kilimanjaro_count + k2_count + everest_count

mousala_percentage = (mousala_count / total) * 100
monblan_percentage = (monblan_count / total) * 100
kilimanjaro_percentage = (kilimanjaro_count / total) * 100
k2_percentage = (k2_count / total) * 100
everest_percentage = (everest_count / total) * 100

print(f'{mousala_percentage:.2f}%')
print(f'{monblan_percentage:.2f}%')
print(f'{kilimanjaro_percentage:.2f}%')
print(f'{k2_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')