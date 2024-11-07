"""
Represent the board game of Tetris
"""

import pygame
import constants
import numpy as np


class Board:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = np.zeros((num_rows, num_cols))
    
    def end_game(self):
        """Checks if the game is still going or not"""
        for col_idx in range(self.num_cols):
            col = self.board[:, col_idx]
            if col == np.ones_like(col): # If a column is filled with ones, the game ends
                return True
        return False


def draw_board(screen):
    """
    Function which draws the Tetris board, without any Tetrimino
    """

    # Draw entire board area including padding
    for row in range(constants.NUM_ROWS + 2 * constants.PADDING):
        for col in range(constants.NUM_COLS + 2 * constants.PADDING):
            x = col * constants.CELL_SIZE
            y = row * constants.CELL_SIZE

            # Check if cell is in the padding area, draw in gray
            if row < constants.PADDING or row >= constants.NUM_ROWS + constants.PADDING or col < constants.PADDING or col >= constants.NUM_COLS + constants.PADDING:
                pygame.draw.rect(screen, constants.GRAY, (x, y, constants.CELL_SIZE, constants.CELL_SIZE))
            # else fill with black rectangles
            else:
                pygame.draw.rect(screen, constants.BLACK, (x, y, constants.CELL_SIZE, constants.CELL_SIZE))
            
            # Draw cell border in white
            pygame.draw.rect(screen, constants.WHITE, (x, y, constants.CELL_SIZE, constants.CELL_SIZE), 1)

    # Color the right zone in white
    pygame.draw.rect(screen, constants.WHITE, (constants.BOARD_WIDTH, 0, constants.WIDTH - constants.BOARD_WIDTH, constants.HEIGHT))


def print_end_game(screen):
    """Displays "Game Over!" whenever the player lost"""

    font = pygame.font.Font(None, 80)  # Set font and size
    text = font.render("Game Over!", True, "red", "white")
    text_rect = text.get_rect(center=(constants.WIDTH // 2, constants.HEIGHT // 2))
    screen.blit(text, text_rect)
