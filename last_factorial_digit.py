import math

factorial_cache = [math.factorial(i) for i in range(11)]
last_digit_cache = list(map(lambda x: str(x)[-1], factorial_cache))

for _ in range(int(input())):
    print(last_digit_cache[int(input())])
