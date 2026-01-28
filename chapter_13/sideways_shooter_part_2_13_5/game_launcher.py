import pygame
from pygame.sprite import Sprite
import sys

from ship import Ship
from bullet import Bullet
from alien import Alien
from setting import Setting

class Game:
    def __init__(self):
        """Initialize the game and set up resources."""
        pygame.init()
        
        self.clock = pygame.time.Clock()

        # Set the screen size (width, height)
        self.setting = Setting()
        self.screen_size = (self.setting.screen_width, self.setting.screen_height)
        self.screen = pygame.display.set_mode(self.screen_size)

        # Get the screen rectangle (used for boundaries and positioning)
        self.screen_rect = self.screen.get_rect()

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _check_events(self):
        """Respond to keyboard and quit events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._key_down_x_y(event)
            elif event.type == pygame.KEYUP:
                self._key_up_x_y(event)

    def _fire_bullets(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _key_down_x_y(self, event):
        """Handle key press events."""
        if event.key == pygame.K_UP:
            self.ship.move_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _key_up_x_y(self, event):
        """Handle key release events."""
        if event.key == pygame.K_UP:
            self.ship.move_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = False

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)

        for bullet in self.bullets.sprites():
                bullet.draw_bullets()

        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)

        alien_width, alien_height = alien.rect.size
        
        # Starting positions for the grid
        alien_position_x = alien_width + alien_width * 5
        alien_x = alien_position_x
        alien_y = alien_height

        # Loop down the screen (rows)
        while alien_y < self.setting.screen_height:
            # Loop across the screen (columns)
            while alien_x < self.setting.screen_width - alien_width:
                self._create_alien(alien_x, alien_y)
                alien_x += alien_width * 2

            # Reset x position and move down to the next row
            alien_x = alien_position_x
            alien_y += alien_height * 2

    def _create_alien(self, alien_x, alien_y):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien.x = alien_x
        alien.rect.x = alien.x
        alien.y = alien_y
        alien.rect.y = alien.y
        self.aliens.add(alien)

    # def _update_aliens(self):
    #     """Update the positions of all aliens in the fleet."""
    #     self.aliens.update()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""

        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.setting.screen_width:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        pygame.sprite.groupcollide(
                        self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.setting.fleet_move_left
        self.setting.fleet_direction *= -1

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

    def run_game(self):
        """Main game loop."""
        while True:
            self._check_events()
            self._update_bullets()

            self.ship.update()
            self._update_aliens()
            self._update_screen()

            self.clock.tick(60)

# Create the game instance and start the game
shooter_ship = Game()
shooter_ship.run_game()