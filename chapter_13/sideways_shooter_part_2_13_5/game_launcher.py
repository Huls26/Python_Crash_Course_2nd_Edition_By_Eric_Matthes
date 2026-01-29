import pygame
import sys

from ship import Ship
from bullet import Bullet
from alien import Alien
from setting import Setting
from game_stats import GameStats

class Game:
    def __init__(self):
        """Initialize the game, settings, and main resources."""
        pygame.init()
        
        # Control the frame rate
        self.clock = pygame.time.Clock()

        # Game settings and screen setup
        self.setting = Setting()
        self.screen_size = (self.setting.screen_width, self.setting.screen_height)
        self.screen = pygame.display.set_mode(self.screen_size)

        # Screen rectangle used for positioning and boundaries
        self.screen_rect = self.screen.get_rect()

        self.stats = GameStats(self)

        # Create the player ship
        self.ship = Ship(self)

        # Sprite groups for bullets and aliens
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Create the initial fleet of aliens
        self._create_fleet()

    def _check_events(self):
        """Handle keyboard input and window close events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._key_down_x_y(event)
            elif event.type == pygame.KEYUP:
                self._key_up_x_y(event)

    def _fire_bullets(self):
        """Create a new bullet fired from the ship."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _key_down_x_y(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_UP:
            self.ship.move_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _key_up_x_y(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.move_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = False

    def _update_screen(self):
        """Redraw the screen and all game elements."""
        self.screen.fill(self.setting.bg_color)

        # Draw bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullets()

        # Draw ship and aliens
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Make the most recent screen visible
        pygame.display.flip()

    def _create_fleet(self):
        """Create a grid-based fleet of aliens starting on the right side."""
        # Create a sample alien to get its size
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        # Starting position for the alien grid
        alien_position_x = alien_width * 6
        alien_x = alien_position_x
        alien_y = alien_height

        # Create multiple rows of aliens
        while alien_y < self.setting.screen_height:
            # Create aliens across the screen
            while alien_x < self.setting.screen_width - alien_width:
                self._create_alien(alien_x, alien_y)
                alien_x += alien_width * 2

            # Move down to the next row
            alien_x = alien_position_x
            alien_y += alien_height * 2

    def _create_alien(self, alien_x, alien_y):
        """Create a single alien at a specific position."""
        alien = Alien(self)
        alien.x = alien_x
        alien.rect.x = alien.x
        alien.y = alien_y
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _update_bullets(self):
        """Update bullets and remove those that leave the screen."""
        self.bullets.update()

        # Remove bullets that move off the right side of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.setting.screen_width:
                self.bullets.remove(bullet)
        
        # Check for bullet–alien collisions
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Remove bullets and aliens that collide."""
        collision = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collision:
            self.stats.alien_hits += 1

        # If all aliens are destroyed, create a new fleet
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Update alien positions (aliens move left toward the ship)."""
        self.aliens.update()

    def run_game(self):
        """Main game loop."""
        while True:
            self._check_events()
            self._update_bullets()

            self.ship.update()
            self._update_aliens()
            self._update_screen()

            # Limit the game to 60 frames per second
            self.clock.tick(60)

# Create the game instance and start the game
shooter_ship = Game()
shooter_ship.run_game()
