input()
task_times = sorted(list(map(int, input().split())))
quiet_times = sorted(list(map(int, input().split())))

quiet_index = 0
completable_tasks = 0
for task_time in task_times:
    while quiet_index < len(quiet_times) and quiet_times[quiet_index] < task_time:
        quiet_index += 1

    if quiet_index < len(quiet_times):
        completable_tasks += 1
        quiet_index += 1
    else:
        break

print(completable_tasks)
