"""
The goal of this file is to represent the pieces of the game : the Tetriminos
"""

# mapping between a letter and its color
COLORS = {
    'I': "aqua",
    'O': "yellow",
    'T': "purple",
    'L': "orange",
    'J': "blue",
    'Z': "red",
    "S": "green"
}

SHAPES = {
    "I": [
        [[1, 1, 1, 1]],
        [[1], [1], [1], [1]]
    ],
    "O": [
        [[0, 1, 1, 0], [0, 1, 1, 0]]
    ],

}

class Tetrimino:
    def __init__(self) -> None:
        pass


    def rotatePiece(self):
        pass