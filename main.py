# Import the pygame module
import pygame
import constants as const
from game_play import GamePlay
from title_screen import TitleScreen
from enum import Enum

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    K_DOWN,
    QUIT,
)
class gameMode(Enum):
    #### GAME MODES ####
    QUIT = 0
    TITLE_SCREEN = 1
    GAME_SCREEN = 2

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))

# Fill the screen with a color
screen.fill((0, 0, 0))

# Update the display
pygame.display.flip()

# Initialize title screen
titleScreen = TitleScreen(screen)

# Start the game mode at the title screen
game_mode = gameMode.TITLE_SCREEN

# Set high score
high_score = 0

while game_mode != gameMode.QUIT:
    while game_mode == gameMode.TITLE_SCREEN:
        for event in pygame.event.get():
            # Did the user click the window close button? If so, stop the loop
            if event.type == QUIT:
                game_mode = gameMode.QUIT

            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    game_mode = gameMode.QUIT

                elif event.key == K_DOWN:
                    # Was it the down arrow? If so, turn on the game_run
                     # Intialize gameplay
                    gamePlay = GamePlay(screen)
                    game_mode = gameMode.GAME_SCREEN
            
        pygame.display.flip()

    while game_mode == gameMode.GAME_SCREEN:
        # play the game
        total_score = gamePlay.playing(screen)

        # This happens after the game/round is done
        game_mode = gameMode.TITLE_SCREEN

        titleScreen.update(screen, total_score, total_score > high_score)

        if total_score > high_score:
            high_score = total_score