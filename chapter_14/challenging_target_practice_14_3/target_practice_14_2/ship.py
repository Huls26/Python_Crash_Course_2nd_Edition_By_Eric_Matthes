import pygame

class Ship:
    """A class to manage the player's ship in the Sideways Shooter game."""

    def __init__(self, game):
        """
        Initialize the ship and set its starting position.

        The ship starts at the left-center of the screen.

        Args:
            game (Game): An instance of the Game class to access screen and settings.
        """
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = game.setting

        # Load the ship image and convert it for faster rendering
        self.rocket = pygame.image.load('../images/cat.bmp').convert()
        
        # Scale the image to the desired size
        self.image = pygame.transform.scale(self.rocket, (75, 80))

        # Get a rect object for positioning
        self.rect = self.image.get_rect()

        # Start the ship at the left-center of the screen
        self.rect.midleft = self.screen_rect.midleft

        # Store the ship's horizontal and vertical positions as floats for smooth movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags for vertical movement
        self.move_up = False
        self.move_down = False

    def center_ship(self):
        """
        Center the ship on the left-center of the screen.

        This is typically called after the ship is hit.
        """
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """
        Update the ship's position based on movement flags.

        Called once per frame.
        Ensures the ship stays within the screen boundaries.
        """
        # Move up if allowed and within screen bounds
        if self.move_up and self.y > 0:
            self.y -= self.setting.ship_speed

        # Move down if allowed and within screen bounds
        if self.move_down and (self.y + self.rect.height) < self.screen_rect.height:
            self.y += self.setting.ship_speed

        # Update the rect position to match the float values
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current position on the screen."""
        self.screen.blit(self.image, self.rect)
