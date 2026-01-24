import pygame
from pygame.sprite import Sprite
import sys

class Star(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the character image 
        # Using an existing image so no need to download another one
        self.star = pygame.image.load('images/star.bmp').convert()
        
        # Scale the image to the desired size
        self.image = pygame.transform.scale(self.star, (50, 50))

        # Get a rect object from the image for positioning
        self.rect = self.image.get_rect()

          # Movement flags for horizontal movement
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store x position as a float for smooth movement
        self.x = float(self.rect.x)

        # Store y position as a float for smooth movement
        self.y = float(self.rect.y)

class Screen:
    def __init__(self):
        """Initialize the game and set up resources."""
        pygame.init()
        
        # Set the screen size (width, height)
        self.screen_width = 750
        self.screen_height = 750
        self.screen_size = (self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode(self.screen_size)

        # Get the screen rectangle (used for boundaries and positioning)
        self.screen_rect = self.screen.get_rect()

        # Background color (white)
        self.bg_color = (255, 255, 255)

        self.stars = pygame.sprite.Group()
        self._create_grid()

    def _check_events(self):
        """Respond to keyboard and quit events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_grid(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.screen_width - (2 * star_width)
        number_star_x = available_space_x // star_width

        # # Determine the number of rows of star that fit on the screen.
        available_space_y = (self.screen_height - (2 * star_height))
        number_rows = available_space_y // star_height

        # Create the first row of aliens.
        for row_number in range(number_rows):
            for star_number in range(number_star_x):
                self._create_star(star_number, row_number)

        # for star_number in range(number_star_x):
        #     self._create_star(star_number) 

    def _create_star(self, star_number, row_number):
        """Create an alien and place it in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star_height + 2 * star_height * row_number
        self.stars.add(star)

    def _update_screen(self):
        self.screen.fill(self.bg_color)

        self.stars.draw(self.screen)
        pygame.display.flip()

    def display_star(self):
        """Main game loop."""
        while True:
            self._check_events()
            self._update_screen()

# Create the game instance and start the game
stars = Screen()
stars.display_star()