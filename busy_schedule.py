while True:
    n = int(input())
    if n == 0:
        break

    appointments = []
    for _ in range(n):
        time, am_pm = input().split()
        hour, minute = list(map(int, time.split(":")))
        if hour == 12:
            hour = 0
        appointments.append((am_pm, hour, minute))
    appointments.sort()

    for appointment in appointments:
        am_pm, hour, minute = appointment
        if hour == 0:
            hour = 12
        print("{}:{:02d} {}".format(hour, minute, am_pm))

    print()