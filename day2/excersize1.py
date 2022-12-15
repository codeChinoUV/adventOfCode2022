
class RockPaperSizorsTornament:
    my_score = 0

    # A, X: Rock
    # B, Y: Paper
    # C, Z: Sizors

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

    def _get_i_win(self, opponent_choice: str, my_choice: str) -> bool:
        return self.defeats_definition[opponent_choice] == my_choice

    def _get_is_a_draw(self, opponent_choice: str, my_choice: str) -> bool:
        return self.draws_definition[opponent_choice] == my_choice

    def _calculate_my_score_from_encrypted_message(self, file_path_with_message: str):
        file = open(file_path_with_message, 'r')
        my_total_score = 0
        for line in file:
            opponent_choice = line[0]
            my_choice = line[2]
            score = 0
            if self._get_i_win(opponent_choice, my_choice):
                score += self.result_points["win"]
            elif self._get_is_a_draw(opponent_choice, my_choice):
                score += self.result_points["draw"]
            else:
                score += self.result_points["lose"]
            score += self.shape_points[my_choice]
            my_total_score += score
        self.my_score = my_total_score

    def __init__(self, file_path_with_message: str) -> None:
        self._calculate_my_score_from_encrypted_message(file_path_with_message)

    def get_my_total_score(self):
        return self.my_score

if __name__ == "__main__":
    tournament = RockPaperSizorsTornament("input.txt")
    print(f"If I use the encripted message i will get the score of {tournament.get_my_total_score()}")