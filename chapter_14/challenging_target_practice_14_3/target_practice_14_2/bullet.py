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
        self.screen_rect = game.screen_rect
        self.ship = game.ship
        self.setting = game.setting

        # Create a bullet rectangle with specified width and height
        # Start at (0,0), then position it at the ship's mid-right
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
        Move the bullet horizontally to the right.

        Updates the float-based x-position and the rect position for rendering.
        Called once per frame in the game loop.
        """
        # Increase the bullet's x position based on the bullet speed
        self.x += self.setting.bullet_speed
        # Update the rect's x-position to match the float value
        self.rect.x = self.x
        
    def draw_bullets(self):
        """Draw the bullet as a filled rectangle on the screen."""
        pygame.draw.rect(
            self.screen,
            self.setting.bullet_color,
            self.rect
        )

    def is_bullet_missed(self):
        # Note: using self.rect.left removes the bullet too early,
        # before it has fully left the screen.

        return self.rect.right >= self.screen_rect.width
