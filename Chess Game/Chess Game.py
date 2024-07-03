class Piece:
    def __init__(self, color):
        self.color = color

    def is_valid_move(self, start, end, board):
        return False

class King(Piece):
    def __str__(self):
        return 'K' if self.color == 'white' else 'k'

class Queen(Piece):
    def __str__(self):
        return 'Q' if self.color == 'white' else 'q'

class Rook(Piece):
    def __str__(self):
        return 'R' if self.color == 'white' else 'r'

class Bishop(Piece):
    def __str__(self):
        return 'B' if self.color == 'white' else 'b'

class Knight(Piece):
    def __str__(self):
        return 'N' if self.color == 'white' else 'n'

class Pawn(Piece):
    def __str__(self):
        return 'P' if self.color == 'white' else 'p'

class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]

        for i in range(8):
            board[1][i] = Pawn('white')
            board[6][i] = Pawn('black')

        placement = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece in enumerate(placement):
            board[0][i] = piece('white')
            board[7][i] = piece('black')

        return board

    def print_board(self):
        for row in self.board:
            print(" ".join([str(piece) if piece else '.' for piece in row]))

    def move_piece(self, start, end):
        start_x, start_y = start
        end_x, end_y = end
        piece = self.board[start_x][start_y]
        if piece and piece.is_valid_move(start, end, self.board):
            self.board[end_x][end_y] = piece
            self.board[start_x][start_y] = None

def get_position(input_str):
    col, row = input_str[0], input_str[1]
    return int(row) - 1, ord(col) - ord('a')

def main():
    board = Board()
    board.print_board()

    while True:
        move = input("Enter your move (e.g., e2 e4): ")
        start_str, end_str = move.split()
        start_pos = get_position(start_str)
        end_pos = get_position(end_str)
        board.move_piece(start_pos, end_pos)
        board.print_board()

if __name__ == '__main__':
    main()
