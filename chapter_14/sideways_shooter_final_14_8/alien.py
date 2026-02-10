import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet for Sideways Shooter."""

    def __init__(self, ai_game):
        """
        Initialize the alien and set its starting position.
        Aliens start near the top-left of the screen and move left toward the player's ship.
        Args:
            ai_game: An instance of the Game class, used to access game settings and the screen.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.setting

        # Load the alien image and get its rectangular area for positioning
        self.image = pygame.image.load('../images/alien.bmp')
        self.rect = self.image.get_rect()

        # Set initial position near the top-left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal and vertical positions as floats for smooth movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the alien left and vertically according to fleet direction."""
        self.x -= 0.2
        self.rect.x = self.x
        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y

    def check_edges(self):
        """Return True if the alien touches the top or bottom of the screen."""
        screen_rect = self.screen.get_rect()

        return self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0
            

    