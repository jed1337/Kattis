from unittest import TestCase

from game_rank import GameRank


class TestGameRank(TestCase):
    def setUp(self) -> None:
        self.game_rank = GameRank()

    def test_calculate_rank_WW(self):
        self.game_rank.calculate_rank("WW")
        self.assertEqual(25, self.game_rank.get_rank())
        self.assertEqual(2, self.game_rank.current_stars)

    def test_calculate_rank_WWW(self):
        self.game_rank.calculate_rank("WWW")
        self.assertEqual(24, self.game_rank.get_rank())
        self.assertEqual(2, self.game_rank.current_stars)

    def test_calculate_rank_WWWW(self):
        self.game_rank.calculate_rank("WWWW")
        self.assertEqual(23, self.game_rank.get_rank())
        self.assertEqual(2, self.game_rank.current_stars)

    def test_calculate_rank_WLWLWLWL(self):
        self.game_rank.calculate_rank("WLWLWLWL")
        self.assertEqual(24, self.game_rank.get_rank())
        self.assertEqual(2, self.game_rank.current_stars)

    def test_calculate_rank_WWWWWWWWWLLWW(self):
        self.game_rank.calculate_rank("WWWWWWWWWLLWW")
        self.assertEqual(19, self.game_rank.get_rank())

    def test_calculate_rank_WWWWWWWWWLWWL(self):
        self.game_rank.calculate_rank("WWWWWWWWWLWWL")
        self.assertEqual(18, self.game_rank.get_rank())

    def test_legend_rank(self):
        self.game_rank.calculate_rank("W"*100)
        self.assertEqual("Legend", self.game_rank.get_rank())

    def test_cannot_lose_legend_rank(self):
        self.game_rank.calculate_rank("{}{}".format("W"*100, "L"*100))
        self.assertEqual("Legend", self.game_rank.get_rank())

    def test_calculate_rank_L(self):
        self.game_rank.calculate_rank("L")
        self.assertEqual(25, self.game_rank.get_rank())

    def test_calculate_rank_no_consecutive_win(self):
        self.game_rank.calculate_rank("WWL"*1000)
        print(self.game_rank.get_rank())

