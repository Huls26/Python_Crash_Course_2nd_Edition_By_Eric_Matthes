import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.ship = game.ship
        self.setting = game.setting

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(
            0, 0, 
            self.setting.bullet_width,
            self.setting.bullet_height)

        self.rect.midright = self.ship.rect.midright
        
        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)
    
    def update(self):
        """Move the bullet up the screen."""

        # Update the decimal position of the bullet.
        self.x += self.setting.bullet_speed
        # Update the rect position.
        self.rect.x = self.x
    
    def draw_bullets(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(
                self.screen,
                self.setting.bullet_color,
                self.rect
            )   
