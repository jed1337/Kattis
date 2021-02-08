"""
Split deliveries from the negative and positive side
Sort the distances by furthest first
For each side,
deliver all letters starting from the furthest distance
if we have some letters left, deliver what we can to the next furthest distance

Solving sample input 1
25 20 | 80 letters left
10 95 | 0 letters left
10 0  | 5 letters left
0 100 | refil at the post
-10 50| 50 letters left
0 100 | refil at the post
"""

DISTANCE_INDEX = 0
LETTERS_INDEX = 1
POST_OFFICE = 0


def get_total_distance(max_capacity, distance_array):
    current_letters = max_capacity
    total_distance = 0
    current_position = POST_OFFICE
    index = 0
    while index < len(distance_array):
        if distance_array[index][LETTERS_INDEX] == 0:
            index += 1
            if index >= len(distance_array):
                break
        if current_position == POST_OFFICE:
            current_letters = max_capacity

        # Go to the furthest house from where we are now
        total_distance += abs(distance_array[index][DISTANCE_INDEX] - current_position)
        current_position = distance_array[index][DISTANCE_INDEX]
        if distance_array[index][LETTERS_INDEX] - current_letters < 0:
            current_letters -= distance_array[index][LETTERS_INDEX]
            distance_array[index][LETTERS_INDEX] = 0
        else:
            distance_array[index][LETTERS_INDEX] -= current_letters
            current_letters = 0
            total_distance += abs(distance_array[index][DISTANCE_INDEX])  # Go back to the post office
            current_position = POST_OFFICE

    if current_position != POST_OFFICE:
        total_distance += abs(current_position - POST_OFFICE)
        current_position = POST_OFFICE

    return total_distance


n, max_capacity = list(map(int, input().split()))
negative_direction = []
positive_direction = []

for _ in range(n):
    distance, letters_required = list(map(int, input().split()))
    if distance < 0:
        negative_direction.append([distance, letters_required])
    else:
        positive_direction.append([distance, letters_required])

negative_direction.sort()
positive_direction.sort(reverse=True)
total_distance = 0

total_distance += get_total_distance(max_capacity, positive_direction)
total_distance += get_total_distance(max_capacity, negative_direction)

print(total_distance)
