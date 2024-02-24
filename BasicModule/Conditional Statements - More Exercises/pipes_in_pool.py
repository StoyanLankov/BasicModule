area_pool = int(input())
pipe_one_per_hour = int(input())
pipe_two_per_hour = int(input())
worker_break_hours = float(input())

pipe_one_total = pipe_one_per_hour * worker_break_hours
pipe_two_total = pipe_two_per_hour * worker_break_hours
total_per_hour = pipe_one_total + pipe_two_total
total_pool = (total_per_hour / area_pool) * 100

first_pipe = (pipe_one_per_hour * worker_break_hours / total_per_hour) * 100
second_pipe = (pipe_two_per_hour * worker_break_hours / total_per_hour) * 100

if total_pool <= 100:
    print(f'The pool is {total_pool:.02f}% full. Pipe 1: {first_pipe:.02f}%. Pipe 2: {second_pipe:.02f}%.')

else:
    difference = total_per_hour - area_pool
    print(f'For {worker_break_hours} hours the pool overflows with {difference:.2f} liters.')