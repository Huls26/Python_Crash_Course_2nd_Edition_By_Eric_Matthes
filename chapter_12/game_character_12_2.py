import pygame
import sys

class DrawCharacter:
    """A class to manage and draw a game character at the center of the screen."""

    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the display window (width, height)
        self.screen = pygame.display.set_mode((720, 720))
        self.screen_rect = self.screen.get_rect()

        self.bg_color = (255, 255, 255)

        # Load the character image
        self.image = pygame.image.load('images/cat.bmp')
        # Scale the image to desired size (width, height)
        self.image = pygame.transform.scale(self.image, (100, 150))
        # Get the rectangle for positioning the image
        self.rect = self.image.get_rect()

        # Start each new character at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the character at its current location on the screen."""
        self.screen.blit(self.image, self.rect)
    
    def run(self):
        """Main loop to keep the window open and display the character."""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Close the window
                    sys.exit()
                elif event.type == pygame.KEYDOWN:  # Key pressed
                    if event.key == pygame.K_q:  # Press 'Q' to quit
                        sys.exit()

            # Fill the screen with a background color
            # Change this to match your image background if needed
            self.screen.fill(self.bg_color)  # White background

            # Draw the character on the screen
            self.blitme()

            # Make the most recently drawn screen visible
            pygame.display.flip()

# Create an instance of DrawCharacter and run the game
display_character = DrawCharacter()
display_character.run()