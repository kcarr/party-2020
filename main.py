# Import the pygame module
import pygame

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    K_DOWN,
    QUIT,
)

from modules.game_play import GamePlay
from modules.game_play import GameMode
from modules.title_screen import TitleScreen
from modules.ui_elements import UIElement
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    TITLE_SCREEN_COLOR,
    TITLE_TEXT_COLOR,
)

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize title screen
titleScreen = TitleScreen(screen)

# Start the game mode at the title screen
game_mode = GameMode.TITLE_SCREEN

# Set high score
high_score = 0

while game_mode != GameMode.QUIT:
    while game_mode == GameMode.TITLE_SCREEN:
        for event in pygame.event.get():
            # Did the user click the window close button? If so, stop the loop
            if event.type == QUIT:
                game_mode = GameMode.QUIT

            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    game_mode = GameMode.QUIT

                elif event.key == K_DOWN:
                    # Was it the down arrow? If so, turn on the game_run
                     # Intialize gameplay
                    gamePlay = GamePlay(screen)
                    game_mode = GameMode.GAME_SCREEN
        
        # Make the start "button"
        start_button = UIElement(
            center_position=(400, 400),
            font_size=50,
            bg_rgb=TITLE_SCREEN_COLOR,
            text_rgb=TITLE_TEXT_COLOR,
            text="START"
        )

        # Make the quit "button"
        quit_button = UIElement(
            center_position=(400, 450),
            font_size=30,
            bg_rgb=TITLE_SCREEN_COLOR,
            text_rgb=TITLE_TEXT_COLOR,
            text="QUIT"
        )

        # Fill the screen with the title color
        screen.fill(TITLE_SCREEN_COLOR)

        start_button.update(pygame.mouse.get_pos())
        start_button.draw(screen)

        quit_button.update(pygame.mouse.get_pos())
        quit_button.draw(screen)

        pygame.display.flip()

    while game_mode == GameMode.GAME_SCREEN:
        # play the game
        total_score = gamePlay.playing(screen)

        # This happens after the game/round is done
        game_mode = GameMode.TITLE_SCREEN

        titleScreen.update(screen, total_score, total_score > high_score)

        if total_score > high_score:
            high_score = total_score