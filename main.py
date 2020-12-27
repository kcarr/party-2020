# Import the pygame module
import pygame

from pygame.sprite import RenderUpdates
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    K_DOWN,
    QUIT,
)

from modules.game_play import GamePlay
from modules.game_play import GameMode
from modules.ui_elements import UIElement
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    TITLE_SCREEN_COLOR,
    TITLE_TEXT_COLOR,
)

def main():
    # Initialize pygame
    pygame.init()

    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the background color
    screen.fill(TITLE_SCREEN_COLOR)
    pygame.display.flip()

    # Start the game mode at the title screen
    game_mode = GameMode.TITLE_SCREEN

    # Initialize the game playing
    game_play = GamePlay(screen)

    # Set high score
    high_score = 0

    while game_mode != GameMode.QUIT:
        if game_mode == GameMode.TITLE_SCREEN:
            game_mode = title_screen(screen)
        
        if game_mode == GameMode.GAME_SCREEN:
            game_mode = game_play.playing(screen)


def title_screen(screen, player=False):
    # Make a Title that is a "button" 
    game_title = UIElement(
        center_position=(400, 200),
        font_size=100,
        bg_rgb=TITLE_SCREEN_COLOR,
        text_rgb=TITLE_TEXT_COLOR,
        text="Party 2020!",
    )
    # Make the start "button"
    start_button = UIElement(
        center_position=(400, 400),
        font_size=50,
        bg_rgb=TITLE_SCREEN_COLOR,
        text_rgb=TITLE_TEXT_COLOR,
        text="START",
        action=GameMode.GAME_SCREEN,
    )

    # Make the quit "button"
    quit_button = UIElement(
        center_position=(400, 450),
        font_size=30,
        bg_rgb=TITLE_SCREEN_COLOR,
        text_rgb=TITLE_TEXT_COLOR,
        text="QUIT",
        action=GameMode.QUIT,
    )

    buttons = RenderUpdates(game_title, start_button, quit_button)

    return title_loop(screen, buttons, fill=TITLE_SCREEN_COLOR)

def title_loop(screen, buttons, fill=(255,255,255)):
    looping = True
    while looping:
        mouse_up = False

        for event in pygame.event.get():
            # Did the user click the window close button? If so, stop the loop
            if event.type == QUIT:
                game_mode = GameMode.QUIT

            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    game_mode = GameMode.QUIT

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        
        screen.fill(fill)
        
        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            
        buttons.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()