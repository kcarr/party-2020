# Import the pygame module
import pygame
import constants as const
import random

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    RLEACCEL,
)

# Define the entity object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Entity(pygame.sprite.Sprite):
    def __init__(self, image_name = "", scale = (25, 25), random = True):
        super(Entity, self).__init__()

        self.surf = self.surf_render(image_name, scale)

        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        
        if random:
            self.rect = self.rect_random()
            self.speed = self.speed_random()
        else:
            self.rect = self.surf.get_rect()
        
    
    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

    def surf_render(self, image_name, scale):
        # load, scale, and convert the image
        entity_image = pygame.image.load(image_name)
        entity_image = pygame.transform.scale(entity_image, scale)
        self.surf = entity_image.convert()

        return self.surf

    def rect_random(self):
        self.rect = self.surf.get_rect(
            center=(
                random.randint(const.SCREEN_WIDTH + 20, const.SCREEN_WIDTH + 100),
                random.randint(const.TITLE_BUFFER, const.SCREEN_PLAY_HEIGHT),
            )
        )

        return self.rect

    def speed_random(self):
        self.speed = random.randint(5, 10)

        return self.speed
