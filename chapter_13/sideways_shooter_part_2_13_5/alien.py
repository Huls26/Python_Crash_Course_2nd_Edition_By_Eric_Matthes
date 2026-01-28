import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet for Sideways Shooter."""

    def __init__(self, ai_game):
        """
        Initialize the alien and set its starting position.
        Aliens start near the top-left of the screen, but will move left toward the ship.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.setting

        # Load the alien image and get its rectangular area for positioning
        self.image = pygame.image.load('../images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top-left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal and vertical positions as floats for smooth movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """
        Move the alien left toward the ship.
        This method is called on every frame to update the alien's position.
        """
        self.x -= self.settings.alien_speed  # Move left
        self.rect.x = self.x  # Update the rect position for rendering
