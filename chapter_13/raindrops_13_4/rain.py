import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    """A class to represent a single star."""

    def __init__(self, game):
        super().__init__()

        # Reference to the main screen
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the star image from the images folder
        self.rain = pygame.image.load('../images/raindrop.bmp')
        
        # Scale the image to a fixed size (50x50 pixels)
        self.image = pygame.transform.scale(self.rain, (50, 50))

        # Get a rect object for positioning the star
        self.rect = self.image.get_rect()

        # Set an initial position (not final grid position yet)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height