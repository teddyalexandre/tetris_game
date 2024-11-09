"""
This file contains the class which manages the board game of Tetris
"""

import pygame
import constants
import numpy as np


class Board:
    """This class manages the events on the game board, the placement of the tetriminoes"""
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = np.zeros((num_rows, num_cols))
        self.colors = np.full((num_rows, num_cols), None)
        self.score = 0
    
    def end_game(self):
        """Checks if the game is still going or not"""
        for col_idx in range(self.num_cols):
            col = self.board[:, col_idx]
            if np.array_equal(col, np.ones_like(col)): # If a column is filled with ones, the game ends
                return True
        return False
    
    def lock_piece(self, tetrimino):
        """Locks the current Tetrimino in place on the board."""
        shape = tetrimino.get_current_shape()
        for row_idx, row in enumerate(shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    # Calculate the board position
                    x = tetrimino.get_position()[0] + col_idx
                    y = tetrimino.get_position()[1] + row_idx
                    # Ensure position is within board limits before locking
                    if 0 <= x < self.num_cols and 0 <= y < self.num_rows:
                        self.board[y, x] = 1  # Mark cell as occupied by setting it to 1
                        self.colors[y, x] = tetrimino.color
    
    def is_valid_position(self, tetrimino):
        """Check if the Tetrimino's position is valid within the board boundaries.
           It also prevents overlapping with other pieces with an offset"""
        shape = tetrimino.get_current_shape()
        for row_idx, row in enumerate(shape):
            for col_idx, cell in enumerate(row):
                # If the cell represents a piece of tetrimino
                if cell:
                    # Calculate its absolute position on the board
                    x = tetrimino.get_position()[0] + col_idx
                    y = tetrimino.get_position()[1] + row_idx


                    # Check boundaries (left, right and down)
                    if x < 0 or x >= self.num_cols or y >= self.num_rows:
                        return False
                    
                    # Check overlap with other pieces already in the board
                    if y >= 0 and self.board[y, x] != 0:
                        return False
        return True
    
    def clear_lines(self):
        """Clears completed lines from the board and returns the number of lines cleared."""
        lines_cleared = 0
        # Check each row from the bottom up
        for row in range(self.num_rows - 1, -1, -1):
            if all(self.board[row, :]):  # Check if row is completely filled
                # Remove the completed line by moving all rows above down by one
                self.board[1:row + 1] = self.board[:row]  # Shift rows down
                self.board[0] = np.zeros(self.num_cols)  # Add an empty row at the top
                # Do the same for colors
                self.colors[1:row + 1] = self.colors[:row]
                self.colors[0] = np.full(self.num_cols, None)
                lines_cleared += 1

        self.score += lines_cleared * 10
        return lines_cleared


    def draw_board(self, screen):
        """
        Function which draws the Tetris board, without any Tetrimino
        """
        # Draw entire board area including padding
        for row in range(constants.NUM_ROWS + 2 * constants.PADDING):
            for col in range(constants.NUM_COLS + 2 * constants.PADDING):
                x = col * constants.CELL_SIZE
                y = row * constants.CELL_SIZE

                # If cell is off-board / in the padding area, draw in gray
                if row < constants.PADDING or row >= constants.NUM_ROWS + constants.PADDING \
                    or col < constants.PADDING or col >= constants.NUM_COLS + constants.PADDING:
                    pygame.draw.rect(screen, constants.GRAY, (x, y, constants.CELL_SIZE, constants.CELL_SIZE))

                # else fill with black rectangles (cell in the board)
                else:
                    pygame.draw.rect(screen, constants.BLACK, (x, y, constants.CELL_SIZE, constants.CELL_SIZE))
                
                # Draw cell borders in white
                pygame.draw.rect(screen, constants.WHITE, (x, y, constants.CELL_SIZE, constants.CELL_SIZE), 1)

        # Color the right zone in white (for the score)
        pygame.draw.rect(screen, constants.WHITE, (constants.BOARD_WIDTH, 0, constants.WINDOW_WIDTH - constants.BOARD_WIDTH, constants.WINDOW_HEIGHT))

    
    def draw_score(self, screen):
        """Displays the score on the screen"""
        font = pygame.font.SysFont("Calibri", 50, True, False)
        score_text = font.render(f"Score = {self.score}", True, constants.BLACK)
        screen.blit(score_text, [550, 440])


    def draw_fixed_pieces(self, screen):
        """Draws the figures that lie already on the board"""
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                if self.colors[row, col]:
                    x = (col + constants.PADDING) * constants.CELL_SIZE
                    y = (row + constants.PADDING) * constants.CELL_SIZE
                    pygame.draw.rect(screen, self.colors[row, col], (x, y, constants.CELL_SIZE, constants.CELL_SIZE))
                    pygame.draw.rect(screen, constants.WHITE, (x, y, constants.CELL_SIZE, constants.CELL_SIZE), 1)

    def print_end_game(self, screen):
        """Displays "Game Over!" whenever the player lost"""
        font = pygame.font.SysFont("Calibri", 100, True, False)  # Set font and size
        text = font.render("Game Over!", True, "red", "white")
        text_rect = text.get_rect(center=(constants.WINDOW_WIDTH // 2, constants.WINDOW_HEIGHT // 2))
        screen.blit(text, text_rect)
