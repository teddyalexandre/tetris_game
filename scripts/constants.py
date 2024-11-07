"""This file comprises the different constants used in the project"""

WIDTH, HEIGHT = 880, 880  # Dimensions of the game window
NUM_ROWS, NUM_COLS = 20, 10  # Number of rows and columns
PADDING = 1  # Padding in terms of cells
CELL_SIZE = 40  # Size of each cell in the game window
BOARD_WIDTH = (NUM_COLS + 2 * PADDING) * CELL_SIZE
BOARD_HEIGHT = (NUM_ROWS + 2 * PADDING) * CELL_SIZE

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