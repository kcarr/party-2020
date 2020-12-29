# This part was adapted from the Programming Pixels post
#  on making a title screen in pygame

import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

class UIElement(Sprite):
    """ A user interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None, reactive=True):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
            action - the GameMode triggered by the button
            reactive - whether the element changes size on scrollover
        """
        self.mouse_over = False

        # create the default image
        default_image = self.create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        if reactive:
            # create the image that shows when mouse is over the element
            highlighted_image = self.create_surface_with_text(
                text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
            )
        else:
            highlighted_image = default_image

        # add both images and their rects to lists
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        self.action = action

        # calls the init method of the parent sprite class
        super().__init__()

    # properties that vary the image and its rect when the mouse is over the element
    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)
    
    def create_surface_with_text(self, text, font_size, text_rgb, bg_rgb):
        """ Returns surface with text written on """
        font = pygame.freetype.SysFont("Courier", font_size, bold=True)

        # render returns two objects: a surface and a rectangle.
        # We only want the surface.
        surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
        return surface.convert_alpha()