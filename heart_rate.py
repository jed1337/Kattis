n = int(input())
for _ in range(n):
    b, p = list(map(float, input().split()))

    bpm = 60 * b / p
    min_abpm = bpm - (60 / p)
    max_abpm = bpm + (60 / p)

    print(min_abpm, bpm, max_abpm)
