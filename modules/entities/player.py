# Import the pygame module
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
)
from os import listdir

from modules.entities.entity import Entity
from constants import (
    SCREEN_WIDTH,
    TITLE_BUFFER,
    SCREEN_PLAY_HEIGHT,
)


# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(Entity):
    def __init__(self):
        Entity.__init__(self, "images/party_gopher/00.png", scale = (60, 60), random = False)
    
    def update(self, pressed_keys):

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= TITLE_BUFFER:
            self.rect.top = TITLE_BUFFER
        if self.rect.bottom >= SCREEN_PLAY_HEIGHT:
            self.rect.bottom = SCREEN_PLAY_HEIGHT
    
    def gifify(self, player_image_index):
        # gifify the party gopher

        # Run gif_pre_processor.py before you do this part
        # get the nth file
        file_list = sorted(listdir("images/party_gopher"))
        file_path = "images/party_gopher/" + file_list[player_image_index % len(file_list)]

        # load, scale, and convert the image
        self.surf = Entity.surf_render(self, file_path, scale = (60, 60))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        