"""
The goal of this file is to represent the pieces of the game : the Tetriminos
"""
import pygame, sys
import board, constants

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

class Tetrimino:
    """This class represents a Tetrimino on the board"""

    def __init__(self, shape, color, position=(5,1), rotation=0):
        """A piece is defined by its shape, its color and its rotated state"""
        self.shape = shape
        self.color = color
        self.position = position
        self.rotation = rotation

    def rotate_piece(self):
        """Rotates the tetrimino depending on its shape
        For example, the shape "O" has only one rotation, while the shape "J" has four ones."""
        self.rotation = (self.rotation + 1) % len(self.shape)
    
    def get_current_shape(self):
        """Returns the state of the tetrimino"""
        return self.shape[self.rotation]
    
    def draw_piece(self):
        current_shape = self.get_current_shape()
        for row_idx, row in enumerate(current_shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    x = (self.position[0] + col_idx) * constants.CELL_SIZE
                    y = (self.position[1] + row_idx) * constants.CELL_SIZE
                    pygame.draw.rect(screen, self.color, (x, y, constants.CELL_SIZE, constants.CELL_SIZE))

        # Draw again the white lines that were deleted by the pieces
        for row in range(constants.NUM_ROWS + 2 * constants.PADDING):
            for col in range(constants.NUM_COLS + 2 * constants.PADDING):
                x = col * constants.CELL_SIZE
                y = row * constants.CELL_SIZE
                pygame.draw.rect(screen, constants.WHITE, (x, y, constants.CELL_SIZE, constants.CELL_SIZE), 1)

# Main game loop

#while True:
# pygame setup
pygame.init()
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Tetris Board")
clock = pygame.time.Clock()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

board.draw_board(screen)
piece_example = Tetrimino(shape=SHAPES["I"], color=COLORS["I"])
piece_example.draw_piece()

pygame.display.flip()
pygame.time.delay(5000)
