from collections import defaultdict

word_limit, job_limit = list(map(int, input().split()))

dictionary = defaultdict(lambda: 0)
for i in range(word_limit):
    word, salary = input().split()
    dictionary[word] = int(salary)

jobs_shown = 0
hay_points = 0
while jobs_shown < job_limit:
    sentence = input()

    if sentence != ".":
        words = sentence.split()
        for word in words:
            hay_points += dictionary[word]
    else:
        jobs_shown += 1
        print(hay_points)

        hay_points = 0
