# Import the pygame module
import pygame
import constants as const
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
)

# Define the toilet paper object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class ToiletPaper(pygame.sprite.Sprite):
    def __init__(self):
        super(ToiletPaper, self).__init__()

        # load, scale, and convert the image
        toilet_paper_image = pygame.image.load("images/toilet_paper.png")
        toilet_paper_image = pygame.transform.scale(toilet_paper_image, (75, 75))
        self.surf = toilet_paper_image.convert()

        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        self.rect = self.surf.get_rect(
            center=(
                random.randint(const.SCREEN_WIDTH + 20, const.SCREEN_WIDTH + 100),
                random.randint(0, const.SCREEN_HEIGHT),
            )
        )

    # Move the toilet paper based on a constant speed
    # Remove the toilet paper when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill