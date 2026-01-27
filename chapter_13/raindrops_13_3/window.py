import pygame
import sys

from rain import Rain

class Window:
    """Overall class to manage the raindrop screen."""

    def __init__(self):
        """Initialize the game and set up resources."""
        pygame.init()
        
        self.clock = pygame.time.Clock()

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

        # Group to store all raindrop sprites
        self.raindrops = pygame.sprite.Group()

        self._create_grid()

    def _check_events(self):
        """Respond to keyboard and quit events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _create_grid(self):
        """Create a full grid of stars on the screen."""

        # Create one raindrop to get its width and height
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

        # Set the raindrop's x and y position
        rain.x = rain_x
        rain.rect.x = rain.x
        rain.y = rain_y
        rain.rect.y = rain.y

        # Add the rain to the sprite group
        self.raindrops.add(rain)

    def _update_screen(self):
        """Redraw the screen and all stars."""

        # Fill the background
        self.screen.fill(self.bg_color)
       
        # Draw all raindrops from the sprite group
        self.raindrops.draw(self.screen)
        
        # Make the most recently drawn screen visible
        pygame.display.flip()

    def display_raindrop(self):
        """Main loop."""
        while True:
            self._check_events()
            for rain in self.raindrops.copy():
                if rain.rect.top >= self.screen_rect.bottom:
                    self.raindrops.remove(rain)
            self.raindrops.update()
            self._update_screen()
           
            self.clock.tick(60)

# Create the instance and start the program
raindrop = Window()
raindrop.display_raindrop()