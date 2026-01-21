import pygame
import sys

class Rocket:
    def __init__(self):
        """Initialize the game and set up resources."""
        pygame.init()
        
        # Set the screen size (width, height)
        self.screen_size = (720, 700)
        self.screen = pygame.display.set_mode(self.screen_size)

        # Get the screen rectangle (used for boundaries and positioning)
        self.screen_rect = self.screen.get_rect()

        # Background color (black)
        self.bg_color = (0, 0, 0)
        
        # Load the character image 
        # Using an existing image so no need to download another one
        self.rocket = pygame.image.load('images/cat.bmp').convert()
        
        # Scale the image to the desired size
        self.image = pygame.transform.scale(self.rocket, (75, 80))

        # Get a rect object from the image for positioning
        self.rect = self.image.get_rect()

        # Start the character at the center of the screen
        self.rect.center = self.screen_rect.center

        # Set the window title
        pygame.display.set_caption("Rocket")

        # Movement flags for horizontal movement
        self.move_right = False
        self.move_left = False
        # Store x position as a float for smooth movement
        self.x = float(self.rect.x)

        # Movement flags for vertical movement
        self.move_up = False
        self.move_down = False
        # Store y position as a float for smooth movement
        self.y = float(self.rect.y)

        # Speed of the rocket (pixels per frame)    
        self.rocket_speed = 0.5

    def update_movement(self):
        """Update the rocket's position based on movement flags."""

        # Move right if allowed and within screen bounds
        if self.move_right and (self.x + self.rect.width) < self.screen_rect.width:
            self.x += self.rocket_speed
        
        # Move left if allowed and within screen bounds
        if self.move_left and self.x > 0:
            self.x -= self.rocket_speed
        
        # Move up if allowed and within screen bounds
        if self.move_up and self.y > 0:
            self.y -= self.rocket_speed
        
        # Move down if allowed and within screen bounds
        if self.move_down and (self.y + self.rect.height) < self.screen_rect.height:
            self.y += self.rocket_speed
        
        # Update the rect position using the float values
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the character at its current position."""
        self.screen.blit(self.image, self.rect)

    def _check_events(self):
        """Respond to keyboard and quit events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._key_down_x_y(event)
            elif event.type == pygame.KEYUP:
                self._key_up_x_y(event)

    def _key_down_x_y(self, event):
        """Handle key press events."""
        if event.key == pygame.K_RIGHT:
            self.move_right = True
        elif event.key == pygame.K_LEFT:
            self.move_left = True
        elif event.key == pygame.K_UP:
            self.move_up = True
        elif event.key == pygame.K_DOWN:
            self.move_down = True
    
    def _key_up_x_y(self, event):
        """Handle key release events."""
        if event.key == pygame.K_RIGHT:
            self.move_right = False
        elif event.key == pygame.K_LEFT:
            self.move_left = False
        elif event.key == pygame.K_UP:
            self.move_up = False
        elif event.key == pygame.K_DOWN:
            self.move_down = False

    def run_game(self):
        """Main game loop."""
        while True:
            self._check_events()

            # Redraw the screen
            self.update_movement()
            self.screen.fill(self.bg_color)
            self.blitme()
            pygame.display.flip()

# Create the game instance and start the game
rocket = Rocket()
rocket.run_game()