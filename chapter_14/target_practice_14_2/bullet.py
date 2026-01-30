import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the player's"""

    def __init__(self, game):
        """
        Initialize a bullet at the ship's current position.

        Bullets are created at the ship's mid-right and move horizontally to the right.

        Args:
            game: An instance of the Game class, used to access the ship, screen, and settings.
        """
        super().__init__()
        self.screen = game.screen
        self.ship = game.ship
        self.setting = game.setting

        # Create a bullet rectangle at (0, 0) with the defined width and height
        # Position it at the ship's mid-right so it appears to be fired from the ship
        self.rect = pygame.Rect(
            0, 0, 
            self.setting.bullet_width,
            self.setting.bullet_height
        )
        self.rect.midright = self.ship.rect.midright

        # Store the bullet's horizontal position as a float for smooth movement
        self.x = float(self.rect.x)

    def update(self):
        """
        Move the bullet right across the screen.

        Called once per frame. Updates the float-based x-position and
        the rect for rendering.
        """
        # Move bullet right based on the bullet speed
        self.x += self.setting.bullet_speed
        # Update rect position for drawing
        self.rect.x = self.x

    def draw_bullets(self):
        """Draw the bullet as a filled rectangle on the screen."""
        pygame.draw.rect(
            self.screen,
            self.setting.bullet_color,
            self.rect
        )
