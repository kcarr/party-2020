import pygame
import constants as const

class TitleScreen():
    def __init__(self, screen):
        # Fill the screen with a color
        screen.fill((0, 255, 0))

        # Update the display
        pygame.display.flip()

    def update(self, screen, score, new_high_score = False):
        if new_high_score:
            print("Hi")
            
        # Fill the screen with a different color
        screen.fill((255,0,0))

        # Update the display
        pygame.display.flip()


