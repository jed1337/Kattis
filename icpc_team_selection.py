datasets = int(input())
for _ in range(datasets):
    team_count = int(input())
    students = sorted(list(map(int, input().split())))

    # We select the team like this: [worst student, 2nd best student, best student]
    # For the median score, we keep on adding the score of the 2nd best student
    median_student_scores = 0
    for i in range(1, team_count + 1):
        median_student_scores += students[-i * 2]

    print(median_student_scores)
