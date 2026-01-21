# Activity: Set the background color to blue
import pygame
import sys

pygame.init()

# set window size
screen = pygame.display.set_mode((780, 720))

# Display the surface with a blue background                         
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 220))
    pygame.display.flip()
