# Import the pygame module
import pygame
import constants as const
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
)


# Define the Virus object by extending pygme.sprite.Sprite
# The surface you draw on the screen is no an attribute of 'Virus'
class Virus(pygame.sprite.Sprite):
    def __init__(self):
        super(Virus, self).__init__()

        # load, scale, and convert the image
        virus_image = pygame.image.load("images/covid.png")
        virus_image = pygame.transform.scale(virus_image, (25, 25))
        self.surf = virus_image.convert()

        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(const.SCREEN_WIDTH + 20, const.SCREEN_WIDTH + 100),
                random.randint(0, const.SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 10)
    
    # Move the sprite based on speed
    # Remove the sprite when it passes the elft edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()