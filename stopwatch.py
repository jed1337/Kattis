times = sorted([int(input()) for _ in range(int(input()))])

if len(times) % 2 == 1:
    print("still running")
else:
    duration = 0
    for i in range(0, len(times), 2):
        start_time = times[i]
        stop_time = times[i + 1]

        duration += stop_time - start_time

    print(duration)
