students_count = int(input())
top_students = 0
between_4_and_4_99 = 0
between_3_and_3_99 = 0
fail_students = 0
total_grade = 0

for _ in range(students_count):
    grade = float(input())
    total_grade += grade

    if grade >= 5.00:
        top_students += 1
    elif grade >= 4.00 and grade <= 4.99:
        between_4_and_4_99 += 1
    elif grade >= 3.00 and grade <= 3.99:
        between_3_and_3_99 += 1
    elif grade < 3.00:
        fail_students += 1

top_students_percentage = (top_students / students_count) * 100
between_4_and_4_99_percentage = (between_4_and_4_99 / students_count) * 100
between_3_and_3_99_percentage = (between_3_and_3_99 / students_count) * 100
fail_students_percentage = (fail_students / students_count) * 100
average_grade = total_grade / students_count

print(f"Top students: {top_students_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_and_4_99_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_and_3_99_percentage:.2f}%")
print(f"Fail: {fail_students_percentage:.2f}%")
print(f"Average: {average_grade:.2f}")
