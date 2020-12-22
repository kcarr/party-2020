# Import the pygame module
import pygame
import constants as const
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
)

# Define the mask object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Mask(pygame.sprite.Sprite):
    def __init__(self):
        super(Mask, self).__init__()

        # load, scale, and convert the image
        mask_image = pygame.image.load("images/mask.png")
        mask_image = pygame.transform.scale(mask_image, (75, 75))
        self.surf = mask_image.convert()

        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        self.rect = self.surf.get_rect(
            center=(
                random.randint(const.SCREEN_WIDTH + 20, const.SCREEN_WIDTH + 100),
                random.randint(0, const.SCREEN_HEIGHT),
            )
        )

    # Move the mask based on a constant speed
    # Remove the mask when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill