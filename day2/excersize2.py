
class RockPaperSizorsTornament:
    my_score = 0

    # A, X: Rock
    # B, Y: Paper
    # C, Z: Sizors
    strategy_definition = {
        "X": "lose",
        "Y": "draw",
        "Z": "win"
    }

    defeats_definition = {
        "A": "Y",
        "B": "Z",
        "C": "X"
    }

    draws_definition = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }

    lose_definition = {
        "A": "Z",
        "B": "X",
        "C": "Y"
    }

    shape_points = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    result_points = {
        "win": 6,
        "draw": 3,
        "lose": 0
    }

    def _get_my_shape_for_win(self, opponent_choice: str) -> str:
        return self.defeats_definition[opponent_choice]

    def _get_my_shape_for_draw(self, opponet_choice: str) -> str:
        return self.draws_definition[opponet_choice]

    def _get_my_shape_for_lose(self, opponent_choice: str) -> str:
        return self.lose_definition[opponent_choice]

    def _calculate_my_score_from_encrypted_message(self, file_path_with_message: str):
        file = open(file_path_with_message, 'r')
        my_total_score = 0
        for line in file:
            opponent_choice = line[0]
            result_needed = self.strategy_definition[line[2]]
            score = 0
            if result_needed == "win":
                my_choice = self._get_my_shape_for_win(opponent_choice)
                score += self.result_points["win"]
            elif result_needed == "draw":
                my_choice = self._get_my_shape_for_draw(opponent_choice)
                score += self.result_points["draw"]
            else:
                my_choice = self._get_my_shape_for_lose(opponent_choice)
                score += self.result_points["lose"]
            score += self.shape_points[my_choice]
            print(result_needed, opponent_choice, my_choice, self.result_points["win"], self.shape_points[my_choice])
            my_total_score += score
        self.my_score = my_total_score

    def __init__(self, file_path_with_message: str) -> None:
        self._calculate_my_score_from_encrypted_message(file_path_with_message)

    def get_my_total_score(self):
        return self.my_score

if __name__ == "__main__":
    tournament = RockPaperSizorsTornament("input.txt")
    print(f"If I use the encripted message i will get the score of {tournament.get_my_total_score()}")