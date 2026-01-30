import pygame
from pygame.sprite import Sprite

class Target(Sprite):
    """A class to represent a single target in the fleet for Sideways Shooter."""

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

        # Store the alien's exact horizontal and vertical positions as floats for smooth movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """
        Move the alien left across the screen.
        
        Called once per frame. Updates both the float-based horizontal position 
        and the rect for rendering on the screen.
        """

        # Move left based on the alien's speed setting
        self.x -= self.setting.alien_speed
        # Update rect position for drawing
        self.rect.x = self.x 

    def draw_target(self):
        """Draw the target as a filled rectangle on the screen."""
        pygame.draw.rect(
            self.screen,
            self.setting.bullet_color,
            self.rect
        )