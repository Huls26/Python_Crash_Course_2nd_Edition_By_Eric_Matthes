import pygame
from pygame.sprite import Sprite
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

        # Store exact position as floats (useful for smooth movement later)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

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
        self._create_grid()

    def _check_events(self):
        """Respond to keyboard and quit events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_grid(self):
        """Create a full grid of stars on the screen."""

        # Create one star to get its size
        star = Star(self)
        star_width, star_height = star.rect.size

        # Calculate available horizontal space
        available_space_x = self.screen_width - (2 * star_width)

        # Calculate how many stars fit per row
        number_star_x = available_space_x // star_width

        # Calculate available vertical space
        available_space_y = (self.screen_height - (2 * star_height))

        # Calculate how many rows fit on the screen
        number_rows = available_space_y // star_height

        # Create stars row by row
        for row_number in range(number_rows):
            for star_number in range(number_star_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Create a star and place it in the correct grid position."""
        star = Star(self)
        star_width, star_height = star.rect.size

        # Calculate the star's x position
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x

        # Calculate the star's y position
        star.rect.y = star_height + 2 * star_height * row_number

        # Add the star to the sprite group
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