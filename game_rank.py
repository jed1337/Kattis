class GameRank():
    def __init__(self):
        self.current_stars = 0
        self.consecutive_wins = 0
        self.current_rank = 25

        self.LEGEND_RANK = 0

    def calculate_rank(self, game_results):
        for game_result in game_results:
            if self.current_rank == self.LEGEND_RANK:
                break

            if game_result == "W":
                self.win()
            else:
                self.lose()

            if not (0 <= self.current_stars <= self.required_stars_per_rank()):
                raise Exception("Invalid stars")

    def win(self):
        self.consecutive_wins += 1
        self.add_star()

        if self.current_stars > self.required_stars_per_rank():
            self.current_stars -= self.required_stars_per_rank()
            self.current_rank -= 1

    def add_star(self):
        self.current_stars += 1
        if self.can_get_bonus_star():
            self.current_stars += 1

    def can_get_bonus_star(self):
        return self.consecutive_wins >= 3 and self.current_rank >= 6

    def lose(self):
        self.consecutive_wins = 0
        if self.current_rank > 20:
            return

        self.subtract_star()
        if self.current_stars == -1:
            if self.current_rank == 20:
                self.current_stars = 0
                return
            self.current_rank += 1
            self.current_stars = self.required_stars_per_rank() - 1

    def subtract_star(self):
        self.current_stars -= 1

    def required_stars_per_rank(self):
        if self.current_rank >= 21:
            return 2
        elif self.current_rank >= 16:
            return 3
        elif self.current_rank >= 11:
            return 4
        elif self.current_rank >= 0:
            return 5
        else:
            raise Exception("Invalid rank")

    def get_rank(self):
        if self.current_rank == self.LEGEND_RANK:
            return "Legend"
        else:
            return self.current_rank


if __name__ == '__main__':
    game_results = input()
    game_rank = GameRank()
    game_rank.calculate_rank(game_results)
    print(game_rank.get_rank())
