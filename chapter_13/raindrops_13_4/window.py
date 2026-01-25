import pygame
import sys

from rain import Rain

class Window:
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
        self.raindrops = pygame.sprite.Group()

        # Create the grid of stars
        self._create_grid()

    def _check_events(self):
        """Respond to keyboard and quit events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_grid(self):
        """Create a full grid of stars on the screen."""

        # Create one star to get its width and height
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        
        # Starting positions for the grid
        rain_x = rain_width
        rain_y = rain_height

        # Loop down the screen (rows)
        while rain_y < self.screen_height - rain_height:

            # Loop across the screen (columns)
            while rain_x < self.screen_width - rain_width:
                self._create_rain(rain_x, rain_y)
                rain_x += rain_width * 2

            # Reset x position and move down to the next row
            rain_x = rain_width
            rain_y += rain_height * 2
        

    def _create_rain(self, rain_x, rain_y):
        """Create a rain and place it in the correct grid position."""
        rain = Rain(self)

        # Set the star's x and y position
        rain.rect.x = rain_x
        rain.rect.y = rain_y

        # Add the star to the sprite group
        self.raindrops.add(rain)

    def _update_screen(self):
        """Redraw the screen and all stars."""

        # Fill the background
        self.screen.fill(self.bg_color)

        # Draw all stars from the sprite group
        self.raindrops.draw(self.screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def display_raindrop(self):
        """Main loop."""
        while True:
            self._check_events()
            self._update_screen()

# Create the instance and start the program
raindrop = Window()
raindrop.display_raindrop()