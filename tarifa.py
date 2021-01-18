megabytes_per_month = int(input())
months = int(input())
megabytes_spent = sum([int(input()) for _ in range(months)])

megabytes_next_month = ((months + 1) * megabytes_per_month) - megabytes_spent
print(megabytes_next_month)