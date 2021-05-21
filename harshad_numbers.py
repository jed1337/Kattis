def is_harshad_number(number):
    digit_sum = sum(map(int, str(number)))
    return number % digit_sum == 0


n = int(input())
while True:
    if is_harshad_number(n):
        print(n)
        break
    else:
        n += 1
