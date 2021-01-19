def get_employees_per_town(town_count):
    employees_per_town = [[] for _ in range(town_count)]

    employee_count = int(input())
    for i in range(employee_count):
        town, drive_count = list(map(int, input().rstrip().split()))
        employees_per_town[town - 1].append(drive_count)

    for i in range(town_count):
        employees_per_town[i].sort(reverse=True)

    return employees_per_town


test_cases = int(input())

for test_case in range(test_cases):
    town_count, office_town = list(map(int, input().rstrip().split()))

    employees_per_town = get_employees_per_town(town_count)

    minimum_cars_per_town = [0] * town_count
    is_possible = True
    for i in range(town_count):
        if (i + 1) == office_town:
            continue

        people_to_drive = len(employees_per_town[i])

        maximum_drive_capacity = sum(employees_per_town[i])

        if maximum_drive_capacity < people_to_drive:
            minimum_cars_per_town[i] = -1
        else:
            minimum_cars = 0
            drive_capacity = 0

            for j in range(len(employees_per_town[i])):
                drive_capacity += employees_per_town[i][j]
                minimum_cars += 1

                if drive_capacity >= people_to_drive:
                    break

            minimum_cars_per_town[i] = minimum_cars

    if -1 in minimum_cars_per_town:
        print("Case #{}: IMPOSSIBLE".format(test_case+1))
    else:
        print("Case #{}: {}".format(test_case+1, " ".join(map(str, minimum_cars_per_town))))
