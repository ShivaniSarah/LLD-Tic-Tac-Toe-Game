from Model.playingPiece import PlayingPiece
from Model.pieceType import PieceType  # Assuming PlayingPiece and PieceType are in the same module/package

class PlayingPieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)
