import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.color = self.setting.bullet_color
        self.ship = ai_game.ship

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(
            0, 0, 
            ai_game.setting.bullet_width,
            ai_game.setting.bullet_height)

        self.rect.midtop = self.ship.rect.midtop
        print(self.rect.midtop)
        
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        # self.shoot_bullet = False

    def update(self):
        """Move the bullet up the screen."""

        # Update the decimal position of the bullet.
        self.y -= self.setting.bullet_speed
        # Update the rect position.
        self.rect.y = self.y
    
    def draw_bullets(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(
                self.screen,
                self.color,
                self.rect
            )   

    def update_alien_bullet(self):
        self.y += self.setting.bullet_speed
        self.rect.y = self.y

        