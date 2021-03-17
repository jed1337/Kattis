import heapq
from unittest import TestCase

from cookie_selection import MedianHeap


class TestMedianHeap(TestCase):

    def setUp(self) -> None:
        self.median_heap = MedianHeap()

    def test_push_even_number_of_elements(self):
        for i in range(1, 11):
            self.median_heap.push(i)

        self._test_heap_contents([-5, -4, -3, -2, -1], [6, 7, 8, 9, 10])

    def test_push_odd_number_of_elements(self):
        for i in range(1, 8):
            self.median_heap.push(i)

        self._test_heap_contents([-3, -2, -1], [4, 5, 6, 7])

    def test_push_pop_1_element(self):
        self.median_heap.push(10)
        self.assertEqual(self.median_heap.lower_half, [])
        self.assertEqual(self.median_heap.upper_half, [10])

        result = self.median_heap.pop()
        self.assertEqual(self.median_heap.lower_half, [])
        self.assertEqual(self.median_heap.upper_half, [])

        self.assertEqual(result, 10)

    def test_push_pop_5_elements(self):
        for i in range(1, 6):
            self.median_heap.push(i)

        self._test_heap_pop([3, 4, 2, 5, 1])

    def _test_heap_contents(self, expected_lower_contents, expected_upper_contents):
        while len(self.median_heap.lower_half) > 0:
            result = heapq.heappop(self.median_heap.lower_half)
            self.assertEqual(result, expected_lower_contents[0])
            expected_lower_contents = expected_lower_contents[1:]

        while len(self.median_heap.upper_half) > 0:
            result = heapq.heappop(self.median_heap.upper_half)
            self.assertEqual(result, expected_upper_contents[0])
            expected_upper_contents = expected_upper_contents[1:]

    def _test_heap_pop(self, expected_medians):
        n = len(expected_medians)
        for i in range(n):
            result = self.median_heap.pop()
            self.assertEqual(result, expected_medians[i])
