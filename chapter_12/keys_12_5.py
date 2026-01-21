import pygame
import sys

# Initialize all imported pygame modules
pygame.init()

# Set the window size (width, height)
screen_size = (720, 700)

# Create the game window
screen = pygame.display.set_mode(screen_size)

# Main game loop (runs forever)
while True:
    # Check all events that happen (keyboard, mouse, quit, etc.)
    for event in pygame.event.get():
        # If the user clicks the close (X) button, exit the program
        if event.type == pygame.QUIT:
            sys.exit()
        
        # If a key is pressed down
        elif event.type == pygame.KEYDOWN:
            # Print the key code of the pressed key
            print(event.key)

    # Update the display (even though nothing is drawn yet)
    pygame.display.flip()