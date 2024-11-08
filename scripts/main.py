"""
This file proceeds to run the Tetris game
"""
import random
import sys
import pygame
import constants 
from board import Board
from tetrimino import Tetrimino

# Initialize Pygame and screen
pygame.init()
pygame.mixer.init()

# Audio management
pygame.mixer.music.load("./audio/Tetris_theme_type_a.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

# Screen configuration
screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
pygame.display.set_caption("Tetris Board")

# Initialize game components
board = Board(constants.NUM_ROWS, constants.NUM_COLS)

# Game settings
clock = pygame.time.Clock()


def pick_random_tetrimino():
    """Picks a tetrimino randomly"""
    letters = list(constants.SHAPES.keys())
    random_letter = random.choice(letters)
    return Tetrimino(shape=constants.SHAPES[random_letter], color=constants.COLORS[random_letter])


def run():
    """
    Play the game until the player loses
    """
    fall_time = 0
    fall_speed = 1000  # milliseconds between automatic falls
    current_tetrimino = pick_random_tetrimino()  # Initial tetrimino

    generate_new = False
    # Main game loop
    while True:
        fall_time += clock.get_rawtime()
        clock.tick()  # Update the clock for frame timing

        # Check for events
        for event in pygame.event.get():
            # If the player quits the window, end everything
            if event.type == pygame.QUIT:
                pygame.mixer.quit()
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
            # If the Tetrimino is blocked or has reached the bottom of the board
            if not current_tetrimino.move_down(board):
                # Lock piece in place
                board.lock_piece(current_tetrimino)

                # Clear the lines if necessary and update the window
                board.clear_lines()
                board.draw_fixed_pieces(screen)
                generate_new = True
            fall_time = 0
        
        if generate_new:
            # Create a new piece
            current_tetrimino = pick_random_tetrimino()
            generate_new = False
            if not board.is_valid_position(current_tetrimino):
                board.print_end_game(screen)
                pygame.display.flip()
                pygame.time.delay(3000)
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()

        # Draw the board, the already placed Tetriminos and the moving one
        board.draw_board(screen)
        board.draw_score(screen)
        board.draw_fixed_pieces(screen)
        current_tetrimino.draw_piece(screen)
        
        pygame.display.flip()  # Update the display


if __name__ == "__main__":
    run()