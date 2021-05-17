limit, group_count = list(map(int, input().split()))

current_people = 0
deny_count = 0
for _ in range(group_count):
    op_code, value = input().split()
    value = int(value)

    if op_code == "enter":
        if current_people + value <= limit:
            current_people += value
        else:
            deny_count += 1
    else:
        current_people -= value

print(deny_count)
