exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute

if arrival_time > exam_time:
    print("Late")
    minutes = arrival_time - exam_time
    hours = minutes // 60
    minutes %= 60
    if hours < 1:
        print(f"{minutes} minutes after the start")
    else:
        print(f"{hours}:{minutes:02d} hours after the start")
elif arrival_time == exam_time:
    print("On time")
elif exam_time - arrival_time <= 30:
    print("On time")
    minutes = exam_time - arrival_time
    print(f"{minutes} minutes before the start")
else:
    print("Early")
    minutes = exam_time - arrival_time
    hours = minutes // 60
    minutes %= 60
    if hours < 1:
        print(f"{minutes} minutes before the start")
    else:
        print(f"{hours}:{minutes:02d} hours before the start")
