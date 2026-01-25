import pygame
from pygame.sprite import Sprite

from random import randint
import sys

class Star(Sprite):
    """A class to represent a single star."""

    def __init__(self, game):
        super().__init__()

        # Reference to the main screen
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the star image from the images folder
        self.star = pygame.image.load('images/star.bmp').convert()
        
        # Scale the image to a fixed size (50x50 pixels)
        self.image = pygame.transform.scale(self.star, (50, 50))

        # Get a rect object for positioning the star
        self.rect = self.image.get_rect()

        # Set an initial position (not final grid position yet)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        

class Screen:
    """Overall class to manage the star screen."""

    def __init__(self):
        """Initialize the game and set up resources."""
        pygame.init()
        
        # Screen dimensions
        self.screen_width = 750
        self.screen_height = 750
        self.screen_size = (self.screen_width, self.screen_height)

        # Create the game window
        self.screen = pygame.display.set_mode(self.screen_size)

        # Get the screen rect for positioning
        self.screen_rect = self.screen.get_rect()

        # Background color (white)
        self.bg_color = (255, 255, 255)

        # Group to store all star sprites
        self.stars = pygame.sprite.Group()

        # Create the grid of stars
        self._create_stars()

    def _check_events(self):
        """Respond to keyboard and quit events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_stars(self):
        """Create a grid of stars using while-loop logic."""

        # Create a sample star to get dimensions
        star = Star(self)
        star_width, star_height = star.rect.size

        # Starting positions
        star_x = star_width
        star_y = star_height

        # Loop down the screen (rows)
        while star_y < self.screen_height - star_height:

            # Loop across the screen (columns)
            while star_x < self.screen_width - star_width:
                self._create_star(star_x, star_y)
                star_x += star_width * 2  # Move to next column

            # Reset x and move to the next row
            star_x = star_width
            star_y += star_height * 2

    def _create_star(self, x, y):
        """Create one star and apply slight random offset."""

        star = Star(self)

        # Apply small random offset for a natural look
        star.rect.x = x + randint(-15, 15)
        star.rect.y = y + randint(-15, 15)

        # Add the star to the group
        self.stars.add(star)

    def _update_screen(self):
        """Redraw the screen and all stars."""

        # Fill the background
        self.screen.fill(self.bg_color)

        # Draw all stars from the sprite group
        self.stars.draw(self.screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def display_star(self):
        """Main loop."""
        while True:
            self._check_events()
            self._update_screen()

# Create the instance and start the program
stars = Screen()
stars.display_star()