"""
This file proceeds to run the Tetris game
"""
import random
import sys
import pygame
import constants  # Assume this includes your constants, like screen dimensions and colors
from board import Board
from tetrimino import Tetrimino  # Assuming these are in separate files

# Initialize Pygame and screen
pygame.init()
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Tetris Board")

# Initialize game components
board = Board(constants.NUM_ROWS, constants.NUM_COLS)

# Game settings
clock = pygame.time.Clock()


def pick_random_tetrimino():
    """Picks a tetrimino randomly"""
    letters = constants.SHAPES.keys()
    random_letter = random.choice(list(letters))
    return Tetrimino(shape=constants.SHAPES[random_letter], color=constants.COLORS[random_letter])


def run():
    """
    Play the game until the player loses
    """
    fall_time = 0
    fall_speed = 1000  # milliseconds between automatic falls
    current_tetrimino = pick_random_tetrimino()

    # Main game loop
    while True:
        screen.fill(constants.BLACK)
        fall_time += clock.get_rawtime()
        clock.tick()  # Update the clock for frame timing

        # Check for events
        for event in pygame.event.get():
            # If the player quits the window, end everything
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # If the player presses a key
            elif event.type == pygame.KEYDOWN:
                # Left movement
                if event.key == pygame.K_LEFT:
                    current_tetrimino.move_left(board)
                # Right movement
                elif event.key == pygame.K_RIGHT:
                    current_tetrimino.move_right(board)
                
                # Down movement
                elif event.key == pygame.K_DOWN:
                    current_tetrimino.move_down(board)

                # Rotation (clockwise)
                elif event.key == pygame.K_UP:
                    current_tetrimino.rotate_piece(board)

        # Automatically move the Tetrimino down
        if fall_time >= fall_speed:
            if not current_tetrimino.move_down(board):
                # Lock piece in place and check for line clears
                #board.lock_piece(current_tetrimino)
                board.clear_lines()
                # Create a new piece
                #current_tetrimino = pick_random_tetrimino()
                if not board.is_valid_position(current_tetrimino):
                    print("Game Over!")
                    pygame.quit()
                    sys.exit()
            fall_time = 0
        

        # Draw the board and current Tetrimino
        board.draw_board(screen)
        current_tetrimino.draw_piece(screen)
        
        pygame.display.flip()  # Update the display


if __name__ == "__main__":
    run()