_, speed_gain, fast_duration = list(map(int, input().split()))
timestamps = list(map(int, input().split()))
timestamps.insert(0, 0)
timestamps.append(fast_duration)

original_duration = 0
speed = 100
for i in range(1, len(timestamps)):
    original_duration += (timestamps[i] - timestamps[i-1]) * speed
    speed += speed_gain

print(original_duration/100)