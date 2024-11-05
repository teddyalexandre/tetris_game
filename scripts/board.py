"""
Represent the board game of Tetris
"""

import pygame
import sys

# Constants
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


# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris Board")
clock = pygame.time.Clock()

def draw_board():
    """
    Function which draws the Tetris board, without any Tetrimino
    """
    
    # Draw entire board area including padding
    for row in range(NUM_ROWS + 2 * PADDING):
        for col in range(NUM_COLS + 2 * PADDING):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            # Check if cell is in the padding area, draw in gray
            if row < PADDING or row >= NUM_ROWS + PADDING or col < PADDING or col >= NUM_COLS + PADDING:
                pygame.draw.rect(screen, GRAY, (x, y, CELL_SIZE, CELL_SIZE))
            # else fill with black rectangles
            else:
                pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE))
            
            # Draw cell border in white
            pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE), 1)

    # Color the right zone in white
    pygame.draw.rect(screen, WHITE, (BOARD_WIDTH, 0, WIDTH - BOARD_WIDTH, HEIGHT))
    

def print_end_game():
    """Displays "Game Over!" whenever the player lost"""

    font = pygame.font.Font(None, 80)  # Set font and size
    text = font.render("Game Over!", True, "red", "white")
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    draw_board()

    pygame.display.flip()