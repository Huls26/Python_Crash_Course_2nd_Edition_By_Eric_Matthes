import pygame
import sys

class Rocket:
    def __init__(self):
        pygame.init()
        
        self.screen_size = (720, 700)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.screen_rect = self.screen.get_rect()

        self.bg_color = (0, 0, 0)
        
        # Load the character image 
        # I used this image so I dont need to download another image
        self.rocket = pygame.image.load('images/cat.bmp').convert()
        # Scale the image to desired size (width, height)
        self.image = pygame.transform.scale(self.rocket, (75, 80))
        # Get the rectangle for positioning the image
        self.rect = self.image.get_rect()

        # Start each new character at the center of the screen.
        self.rect.center = self.screen_rect.center

        pygame.display.set_caption("Rocket")

        self.move_right = False
        self.move_left = False
        self.x = float(self.rect.x)

        self.move_up = False
        self.move_down = False
        self.y = float(self.rect.y)

        self.rocket_speed = 0.5

    def update_movement(self):
        if self.move_right and (self.x + self.rect.width) < self.screen_rect.width:
            self.x += self.rocket_speed
        if self.move_left and self.x > 0:
            self.x -= self.rocket_speed
        if self.move_up and self.y > 0:
            self.y -= self.rocket_speed
        if self.move_down and (self.y + self.rect.height) < self.screen_rect.height:
            self.y += self.rocket_speed
        
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the character at its current location on the screen."""
        self.screen.blit(self.image, self.rect)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._key_down_x_y(event)
            elif event.type == pygame.KEYUP:
                self._key_up_x_y(event)

    def _key_down_x_y(self, event):
        if event.key == pygame.K_RIGHT:
            self.move_right = True
        elif event.key == pygame.K_LEFT:
            self.move_left = True
        elif event.key == pygame.K_UP:
            self.move_up = True
        elif event.key == pygame.K_DOWN:
            self.move_down = True
    
    def _key_up_x_y(self, event):
        if event.key == pygame.K_RIGHT:
            self.move_right = False
        elif event.key == pygame.K_LEFT:
            self.move_left = False
        elif event.key == pygame.K_UP:
            self.move_up = False
        elif event.key == pygame.K_DOWN:
            self.move_down = False

    def run_game(self):
        while True:
            self._check_events()

            self.update_movement()
            self.screen.fill(self.bg_color)
            self.blitme()
            pygame.display.flip()

rocket = Rocket()
rocket.run_game()