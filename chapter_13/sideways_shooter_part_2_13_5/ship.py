import pygame

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.setting = game.setting

        # Load the character image 
        # Using an existing image so no need to download another one
        self.rocket = pygame.image.load('../images/cat.bmp').convert()
        
        # Scale the image to the desired size
        self.image = pygame.transform.scale(self.rocket, (75, 80))

        # Get a rect object from the image for positioning
        self.rect = self.image.get_rect()

        # Start the character at the center of the screen
        self.rect.midleft = self.screen_rect.midleft

        # Store x position as a float for smooth movement
        self.x = float(self.rect.x)

        # Movement flags for vertical movement
        self.move_up = False
        self.move_down = False
        # Store y position as a float for smooth movement
        self.y = float(self.rect.y)

        # Speed of the rocket (pixels per frame)    

    def update(self):
        """Update the rocket's position based on movement flags."""
        
        # Move up if allowed and within screen bounds
        if self.move_up and self.y > 0:
            self.y -= self.setting.ship_speed
        
        # Move down if allowed and within screen bounds
        if self.move_down and (self.y + self.rect.height) < self.screen_rect.height:
            self.y +=  self.setting.ship_speed
        
        # Update the rect position using the float values
        self.rect.y = self.y

    def blitme(self):
        """Draw the character at its current position."""
        self.screen.blit(self.image, self.rect)
