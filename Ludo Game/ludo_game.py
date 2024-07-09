import random

class LudoGame:
    def __init__(self):
        self.board = {
            'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0,
            'Y1': 0, 'Y2': 0, 'Y3': 0, 'Y4': 0,
            'G1': 0, 'G2': 0, 'G3': 0, 'G4': 0,
            'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0,
        }
        self.players = ['Red', 'Yellow', 'Green', 'Blue']
        self.positions = {player: {'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0} for player in self.players}
        self.home = {player: ['R1', 'R2', 'R3', 'R4'] for player in self.players}
        self.finish_line = {player: 0 for player in self.players}
        self.winning_score = 4  # Number of tokens to move to finish line to win

    def roll_dice(self):
        return random.randint(1, 6)

    def move_token(self, player, token, steps):
        current_position = self.positions[player][token]
        if current_position in self.home[player]:
            if steps == 6:
                self.positions[player][token] = player[0] + 'S1'
                self.home[player].remove(current_position)
            return

        if current_position.startswith(player[0] + 'S'):
            new_position = int(current_position[2:]) + steps
            if new_position <= 51:
                self.positions[player][token] = player[0] + 'S' + str(new_position)
            elif new_position - 51 <= steps:
                self.positions[player][token] = player[0] + str(new_position - 51)
                self.finish_line[player] += 1

    def display_board(self):
        print("Ludo Game Board:")
        for player in self.players:
            print(f"{player} Home: {self.home[player]}, Finish Line: {self.finish_line[player]}")
            print(f"{player} Positions: {self.positions[player]}")
        print()

    def play(self):
        while max(self.finish_line.values()) < self.winning_score:
            for player in self.players:
                input(f"{player}'s turn (Press Enter to roll dice)")
                dice = self.roll_dice()
                print(f"{player} rolled: {dice}")
                
                if dice == 6 and self.home[player]:
                    token = self.home[player].pop(0)
                    self.positions[player][token] = player[0] + 'S1'
                elif self.positions[player]:
                    token = random.choice(list(self.positions[player].keys()))
                    self.move_token(player, token, dice)
                
                self.display_board()

        winner = [player for player, score in self.finish_line.items() if score == self.winning_score][0]
        print(f"Congratulations! {winner} wins the game!")

if __name__ == "__main__":
    game = LudoGame()
    game.play()
