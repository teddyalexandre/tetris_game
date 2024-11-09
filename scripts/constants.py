"""This file gathers the different constants used in the project"""

WINDOW_WIDTH, WINDOW_HEIGHT = 880, 880  # Dimensions of the whole window
NUM_ROWS, NUM_COLS = 20, 10  # Number of rows and columns of the board
PADDING = 1  # Padding size of the board
CELL_SIZE = 40  # Size of each cell in the window
BOARD_WIDTH = (NUM_COLS + 2 * PADDING) * CELL_SIZE  # Width occupied by the board in the whole window
BOARD_HEIGHT = (NUM_ROWS + 2 * PADDING) * CELL_SIZE # Height occupied by the board in the whole window

# Colors
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
WHITE = (255, 255, 255)

# mapping between a letter and its colors
COLORS = {
    'I': "aqua",
    'O': "yellow",
    'T': "purple",
    'L': "orange",
    'J': "blue",
    'Z': "red",
    "S": "green"
}

# mapping the tetriminos and their rotations
SHAPES = {
    "I": [
        [[1, 1, 1, 1]],
        [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]]
    ],
    "O": [
        [[0, 1, 1, 0], [0, 1, 1, 0]]
    ],
    "S": [
        [[0, 1, 1, 0], [1, 1, 0, 0]],
        [[0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0]]
    ],
    "Z": [
        [[1, 1, 0, 0], [0, 1, 1, 0]],
        [[0, 1, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
    ],
    "L": [
        [[0, 0, 1, 0], [1, 1, 1, 0]],
        [[1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0]],
        [[1, 1, 1, 0], [1, 0, 0, 0]],
        [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]]
    ],
    "J": [
        [[1, 0, 0, 0], [1, 1, 1, 0]],
        [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]],
        [[1, 1, 1, 0], [0, 0, 1, 0]],
        [[0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 1, 0]]
    ],
    "T": [
        [[0, 1, 0, 0], [1, 1, 1, 0]],
        [[0, 1, 0, 0], [0, 1, 1, 0], [0, 1, 0, 0]],
        [[1, 1, 1, 0], [0, 1, 0, 0]],
        [[0, 1, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]]
    ]
}
