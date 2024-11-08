"""
This file codes the representation of the pieces of the game : the Tetriminos
"""

import pygame
import constants

INITIAL_POSITION = ((constants.NUM_COLS - 1) // 2, constants.PADDING)

class Tetrimino:
    """This class represents a Tetrimino on the board"""

    def __init__(self, shape, color, position=INITIAL_POSITION, rotation=0):
        """A tetrimino is defined by its shape, its color and its rotated state"""
        self.shape = shape
        self.color = color
        self.position = position
        self.rotation = rotation
    
    def get_position(self):
        """Access to the position of the tetrimino"""
        return self.position

    def get_current_shape(self):
        """Returns the state of the tetrimino"""
        return self.shape[self.rotation]
    
    def rotate_piece(self, board_game):
        """Rotates the tetrimino depending on its shape
           For example, the shape "O" has only one rotation, while the shape "J" has four ones.
           The rotation is canceled if the piece gets in a invalid position
        """
        self.rotation = (self.rotation + 1) % len(self.shape)
        # Revert rotation if it's not valid
        if not board_game.is_valid_position(self):
            self.rotation = (self.rotation - 1) % len(self.shape)
        
    def move_left(self, board_game):
        """Move piece left if there is no collision."""
        self.position = (self.position[0] - 1, self.position[1])
        if not board_game.is_valid_position(self):
            self.position = (self.position[0] + 1, self.position[1])
            return 0
        return 1

    def move_right(self, board_game):
        """Move piece right if there is no collision."""
        self.position = (self.position[0] + 1, self.position[1])
        if not board_game.is_valid_position(self):
            self.position = (self.position[0] - 1, self.position[1])
            return 0
        return 1

    def move_down(self, board_game):
        """Move piece down if there is no collision."""
        self.position = (self.position[0], self.position[1] + 1)
        
        # Handle case when piece can't move down (lock piece or spawn new one)
        if not board_game.is_valid_position(self):
            self.position = (self.position[0], self.position[1] - 1)
            return 0
        return 1            

    def draw_piece(self, screen):
        """This function draws the figure in the game board at its initial position"""
        current_shape = self.get_current_shape()
        for row_idx, row in enumerate(current_shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    x = (self.position[0] + col_idx + constants.PADDING) * constants.CELL_SIZE
                    y = (self.position[1] + row_idx + constants.PADDING) * constants.CELL_SIZE
                    pygame.draw.rect(screen, self.color, (x, y, constants.CELL_SIZE, constants.CELL_SIZE))

        # Draw again the white lines that were deleted by the pieces
        for row in range(constants.NUM_ROWS + 2 * constants.PADDING):
            for col in range(constants.NUM_COLS + 2 * constants.PADDING):
                x = col * constants.CELL_SIZE
                y = row * constants.CELL_SIZE
                pygame.draw.rect(screen, constants.WHITE, (x, y, constants.CELL_SIZE, constants.CELL_SIZE), 1)

