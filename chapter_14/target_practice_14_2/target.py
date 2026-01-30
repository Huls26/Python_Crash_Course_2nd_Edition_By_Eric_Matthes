import pygame
from pygame.sprite import Sprite

class Target(Sprite):
    """A class to represent a single target"""

    def __init__(self, ai_game):
        """
        Initialize the target and set its starting position.
        targets start near the top-left of the screen and move left toward the player's ship.
        Args:
            ai_game: An instance of the Game class, used to access game settings and the screen.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = ai_game.setting

        # Load the target image and get its rectangular area for positioning
        self.rect = pygame.Rect(
            0, 0, 
            self.setting.target_width,
            self.setting.target_height
        )

        # Set initial position near the top-left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Position the target at the middle-right of the screen
        # using rect.right and rect.centery for precise alignment
        self.rect.right = self.screen_rect.right - self.rect.width
        self.rect.centery = self.screen_rect.centery

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if target is at edge of screen."""
        return self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0

    def update(self):
        """
        Move the target up and down the screen.
        
        Called once per frame. Updates both the float-based vertical position 
        and the rect for rendering on the screen.
        """

        # Move left based on the alien's speed setting
        self.y += self.setting.target_speed * self.setting.target_direction
        # Update rect position for drawing
        self.rect.y = self.y 

    def draw_target(self):
        """Draw the target as a filled rectangle on the screen."""
        pygame.draw.rect(
            self.screen,
            self.setting.target_color,
            self.rect
        )