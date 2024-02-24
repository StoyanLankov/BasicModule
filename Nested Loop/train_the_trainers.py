jury_count = int(input())
total_assessment = 0
presentation_count = 0

while True:
    presentation = input()
    if presentation == "Finish":
        break

    presentation_sum = 0
    for _ in range(jury_count):
        assessment = float(input())
        presentation_sum += assessment

    average_assessment = presentation_sum / jury_count
    total_assessment += average_assessment
    presentation_count += 1

    print(f"{presentation} - {average_assessment:.2f}.")

final_assessment = total_assessment / presentation_count
print(f"Student's final assessment is {final_assessment:.2f}.")
