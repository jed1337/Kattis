"""
We need to keep a list of sorted elements.
When the input is #, we get the median element from the list

if L is a sorted list of size n,
self.lower_half is a max heap that contains the first n/2 elements
self.upper_half is a min heap that contains the last n/2 elements

The median element will always be self.upper_half[0]
"""

import heapq


class MedianHeap:

    def __init__(self):
        self.upper_half = []
        self.lower_half = []

    def pop(self):
        result = heapq.heappop(self.upper_half)
        self._recalculate_heaps()

        return result

    def push(self, value):
        median = self._get_median()
        if value > median:
            heapq.heappush(self.upper_half, value)
        else:
            heapq.heappush(self.lower_half, -value)

        self._recalculate_heaps()

    def _get_median(self):
        if len(self.upper_half) == 0 and len(self.lower_half) == 0:
            return -1

        return self.upper_half[0]

    def _recalculate_heaps(self):
        while len(self.lower_half) - len(self.upper_half) < -1:
            result = heapq.heappop(self.upper_half)
            heapq.heappush(self.lower_half, -result)
        while len(self.lower_half) - len(self.upper_half) > 0:
            result = heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, -result)


median_heap = MedianHeap()

if __name__ == '__main__':
    try:
        while True:
            line = input()
            if not line:
                break

            if line == "#":
                print(median_heap.pop())
            else:
                median_heap.push(int(line))
    except EOFError:
        pass
