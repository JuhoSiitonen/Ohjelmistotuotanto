class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def even_score(self):
        if self.player1_score == 0:
            self.score = "Love-All"
        elif self.player1_score == 1:
            self.score = "Fifteen-All"
        elif self.player1_score == 2:
            self.score = "Thirty-All"
        else:
            self.score = "Deuce"

    def end_of_game(self):
        minus_result = self.player1_score - self.player2_score
        if minus_result == 1:
            self.score = "Advantage player1"
        elif minus_result == -1:
            self.score = "Advantage player2"
        elif minus_result >= 2:
            self.score = "Win for player1"
        else:
            self.score = "Win for player2"

    def single_score(self, temp_score):
        if temp_score == 0:
                self.score = self.score + "Love"
        elif temp_score == 1:
            self.score = self.score + "Fifteen"
        elif temp_score == 2:
            self.score = self.score + "Thirty"
        elif temp_score == 3:
            self.score = self.score + "Forty"

    def compile_normal_score(self):
        self.single_score(self.player1_score)
        self.score = self.score + "-"
        self.single_score(self.player2_score)

    def get_score(self):
        self.score = ""

        if self.player1_score == self.player2_score:
            self.even_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            self.end_of_game()
        else:
            self.compile_normal_score()

        return self.score
