import pygame
import sys

class DrawCharacter:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((720, 720))
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/cat.bmp')
        self.image = pygame.transform.scale(self.image, (100, 150)) 
        self.rect = self.image.get_rect()

        # Start each new character at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
    
    def run(self):
        while True:
             # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

            self.screen.fill((255, 255, 255))
            
            self.blitme()

            # Make the most recently drawn screen visible.                        
            pygame.display.flip()

display_charactere = DrawCharacter()
display_charactere.run()