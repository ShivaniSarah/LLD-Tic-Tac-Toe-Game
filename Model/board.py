from typing import List, Tuple
from Model.pieceType import PieceType
from Model.playingPiece import PlayingPiece

class PieceType:
    X = "X"
    O = "O"

class PlayingPiece:
    def __init__(self, piece_type):
        self.piece_type = piece_type

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None] * size for _ in range(size)]

    def add_piece(self, row, column, playing_piece):
        if self.board[row][column] is not None:
            return False
        self.board[row][column] = playing_piece
        return True

    def get_free_cells(self) -> List[Tuple[int, int]]:
        free_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] is None]
        return free_cells

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is not None:
                    print(f"{self.board[i][j].piece_type}   ", end="")
                else:
                    print("    ", end="")
                print(" | ", end="")
            print()

# # Example usage:
# if __name__ == "__main__":
#     size = 3  # Set the board size
#     board = Board(size)
    
#     # Example: Add X and O to the board
#     x_piece = PlayingPiece(PieceType.X)
#     o_piece = PlayingPiece(PieceType.O)
    
#     board.add_piece(0, 0, x_piece)
#     board.add_piece(1, 1, o_piece)
    
#     # Print the board
#     board.print_board()
    
#     # Get free cells
#     free_cells = board.get_free_cells()
#     print("Free Cells:", free_cells)
