# Algorithm:
# Put the activities in a priority queue, aHeap
#   root node = minimum finishing time
# Put all classrooms in a priority queue, cHeap
#   root node = class room with the minimum available time
#
# While we have activities:
#   Get the earliest finishing activity
#   Put it in the earliest classroom that's available
#   If it was put in a classroom, update the classroom's next available time
#   Else, the activity can't fit in all the rooms, so ignore it
#
# Code
# activity_count = 0
# while aHeap not empty:
#   result = pop aHeap
#   free_room = peek cHeap
#   if we can put result in free_room:
#       pop cHeap
#       free_room.ending_time = result.ending_time
#       cHeap.push free_room
#       activity_count += 1
# print activity_count

import heapq

activity_count, classroom_count = list(map(int, input().split()))

activities = []
for _ in range(activity_count):
    start, end = list(map(int, input().split()))
    # Order by earliest end time, then earliest start time
    heapq.heappush(activities, (end, start))

classrooms = [0] * classroom_count

can_schedule = 0
while len(activities) > 0:
    early_end, early_start = heapq.heappop(activities)
    free_room = classrooms[0]
    if early_end > free_room and early_start > free_room:
        heapq.heappop(classrooms)
        heapq.heappush(classrooms, early_end)
        can_schedule += 1

print(can_schedule)