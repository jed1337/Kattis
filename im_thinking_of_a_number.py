class ClueFormatter:
    def __init__(self, clues):
        self.less_than = 50001
        self.greater_than = 0
        self.divisible_by = []

        for clue in clues:
            op_code, _, number = clue.split()
            number = int(number)

            if op_code == "less":
                if self.less_than == 50001:
                    self.less_than = number
                else:
                    self.less_than = min(self.less_than, number)
            elif op_code == "greater":
                self.greater_than = max(self.greater_than, number)
            else:
                self.divisible_by.append(number)


if __name__ == '__main__':
    while True:
        number = int(input())
        if number == 0:
            break

        clues = [input() for _ in range(number)]
        clue_formatter = ClueFormatter(clues)

        if clue_formatter.less_than == 50001:
            print("infinite")
            continue

        answers = []
        for i in range(clue_formatter.greater_than + 1, clue_formatter.less_than):
            is_divisible = all(map(lambda divisor: i % divisor == 0, clue_formatter.divisible_by))
            if is_divisible:
                answers.append(i)

        if answers:
            print(" ".join(map(str, answers)))
        else:
            print("none")
