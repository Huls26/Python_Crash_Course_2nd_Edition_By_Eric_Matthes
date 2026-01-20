import sys
import pygame

from setting import Setting
from ship import Ship
from space_ship import SpaceShip

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        
        self.setting = Setting()

        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height))
        
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.space_ship = SpaceShip(self)
    
    def _check_events(self):
        # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # Move the ship to the right.
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.rect.x -= 20
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False

    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.setting.bg_color)
        
        self.ship.blitme()
        self.ship.update()
        self.space_ship.blitme()

        # Make the most recently drawn screen visible.                        
        pygame.display.flip()
         
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
                
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()