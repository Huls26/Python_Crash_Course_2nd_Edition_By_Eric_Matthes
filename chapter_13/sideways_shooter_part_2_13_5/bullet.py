import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship in the Sideways Shooter game."""

    def __init__(self, game):
        """
        Initialize a bullet at the ship's current position.
        Bullets will move horizontally to the right across the screen.
        """
        super().__init__()
        self.screen = game.screen
        self.ship = game.ship
        self.setting = game.setting

        # Create a bullet rectangle (width x height) at (0,0)
        # Position it at the ship's mid-right so it appears to be fired from the ship
        self.rect = pygame.Rect(
            0, 0, 
            self.setting.bullet_width,
            self.setting.bullet_height
        )
        self.rect.midright = self.ship.rect.midright

        # Store the bullet's horizontal position as a float for precise movement
        self.x = float(self.rect.x)

    def update(self):
        """
        Move the bullet to the right across the screen.
        This method is called once per frame to update the bullet's position.
        """
        # Increase the x-coordinate by the bullet speed to move it right
        self.x += self.setting.bullet_speed
        # Update the rect position to match the float position
        self.rect.x = self.x

    def draw_bullets(self):
        """Draw the bullet as a rectangle on the screen."""
        pygame.draw.rect(
            self.screen,
            self.setting.bullet_color,
            self.rect
        )
