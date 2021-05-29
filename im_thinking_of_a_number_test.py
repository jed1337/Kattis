from unittest import TestCase

from im_thinking_of_a_number import ClueFormatter


class TestClueFormatter(TestCase):
    def test_default_values(self):
        clue_formatter = ClueFormatter([])

        self.assertEqual(clue_formatter.less_than, 50001)
        self.assertEqual(clue_formatter.greater_than, 0)
        self.assertEqual(clue_formatter.divisible_by, [])

    def test_can_read_clues(self):
        clues = [
            "less than 100",
            "greater than 5",
            "divisible by 7"
        ]

        clue_formatter = ClueFormatter(clues)
        self.assertEqual(clue_formatter.less_than, 100)
        self.assertEqual(clue_formatter.greater_than, 5)
        self.assertEqual(clue_formatter.divisible_by, [7])

    def test_less_than(self):
        clues = [
            "less than 200",
            "less than 100",
            "less than 150",
        ]

        clue_formatter = ClueFormatter(clues)
        self.assertEqual(clue_formatter.less_than, 100)

    def test_greater_than(self):
        clues = [
            "greater than 6",
            "greater than 400",
            "greater than 100",
            "greater than 7"
        ]

        clue_formatter = ClueFormatter(clues)
        self.assertEqual(clue_formatter.greater_than, 400)

    def test_divisible_by(self):
        clues = [
            "divisible by 1",
            "divisible by 5",
            "divisible by 3",
            "divisible by 2"
        ]

        clue_formatter = ClueFormatter(clues)
        self.assertEqual(clue_formatter.divisible_by, [1, 5, 3, 2])
