import pygame
from pygame.sprite import Sprite
import sys

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the character image 
        # Using an existing image so no need to download another one
        self.rocket = pygame.image.load('images/cat.bmp').convert()
        
        # Scale the image to the desired size
        self.image = pygame.transform.scale(self.rocket, (75, 80))

        # Get a rect object from the image for positioning
        self.rect = self.image.get_rect()

        # Start the character at the center of the screen
        self.rect.bottomleft = self.screen_rect.bottomleft

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

    def update(self):
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

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.ship = game.ship

         # Bullet settings
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(
            0, 0, 
            self.bullet_width,
            self.bullet_height)

        self.rect.midright = self.ship.rect.midright
        
        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)
    
    def update(self):
        """Move the bullet up the screen."""

        # Update the decimal position of the bullet.
        self.x += self.bullet_speed
        # Update the rect position.
        self.rect.x = self.x
    
    def draw_bullets(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(
                self.screen,
                self.bullet_color,
                self.rect
            )   


class Game:
    def __init__(self):
        """Initialize the game and set up resources."""
        pygame.init()
        
        # Set the screen size (width, height)
        self.screen_size = (720, 700)
        self.screen = pygame.display.set_mode(self.screen_size)

        # Get the screen rectangle (used for boundaries and positioning)
        self.screen_rect = self.screen.get_rect()

        # Background color (white)
        self.bg_color = (255, 255, 255)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def _check_events(self):
        """Respond to keyboard and quit events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._key_down_x_y(event)
            elif event.type == pygame.KEYUP:
                self._key_up_x_y(event)

    def _fire_bullets(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _key_down_x_y(self, event):
        """Handle key press events."""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_UP:
            self.ship.move_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
            
    def _key_up_x_y(self, event):
        """Handle key release events."""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False
        elif event.key == pygame.K_UP:
            self.ship.move_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = False

    def _update_screen(self):
        self.screen.fill(self.bg_color)

        for bullet in self.bullets.sprites():
                bullet.draw_bullets()

        self.ship.blitme()
        pygame.display.flip()

    def run_game(self):
        """Main game loop."""
        while True:
            self._check_events()
            self.bullets.update()

            # Remove bullets that have gone off the screen
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
                    # Remove bullets that have gone off the screen
            self.ship.update()
            self._update_screen()

# Create the game instance and start the game
shooter_ship = Game()
shooter_ship.run_game()