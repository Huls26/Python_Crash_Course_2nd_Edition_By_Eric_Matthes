import pygame
import sys
from time import sleep

from ship import Ship
from bullet import Bullet
from target import Target
from setting import Setting
from game_stats import GameStats

class Game:
    """Overall class to manage game assets and behavior for Sideways Shooter."""

    def __init__(self):
        """Initialize the game, settings, screen, ship, bullets, aliens, and statistics."""
        pygame.init()
        
        # Control the frame rate
        self.clock = pygame.time.Clock()

        # Game settings and screen setup
        self.setting = Setting()
        self.screen_size = (self.setting.screen_width, self.setting.screen_height)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.screen_rect = self.screen.get_rect()

        # Game statistics
        self.stats = GameStats(self)

        # Create the player ship
        self.ship = Ship(self)

        # Sprite groups for bullets and aliens
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)

    def _check_events(self):
        """Respond to keyboard and mouse events."""
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
        """Handle key press events for ship movement and firing."""
        if event.key == pygame.K_UP:
            self.ship.move_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif event.key == pygame.K_SPACE and self.stats.game_active:
            self._fire_bullets()
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _key_up_x_y(self, event):
        """Handle key release events to stop ship movement."""
        if event.key == pygame.K_UP:
            self.ship.move_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = False

    def _update_screen(self):
        """Redraw all game elements on the screen each frame."""
        self.screen.fill(self.setting.bg_color)

        # Draw bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullets()

        # Draw ship and target
        self.ship.blitme()
        self.target.draw_target()

        # Make the most recent screen visible
        pygame.display.flip()

    def _update_bullets(self):
        """Update the position of bullets and remove those that have moved off-screen."""
        self.bullets.update()

        # Remove bullets that move off the right side of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.setting.screen_width:
                self.bullets.remove(bullet)
        
        # Check for collisions between bullets and aliens
        # self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """
        Detect collisions between bullets and aliens, remove them, and update alien hit count.

        Also ends the game if max_alien_hits is reached, and creates a new fleet if all aliens are destroyed.
        
        """
        collision = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        for aliens_hit in collision.values():
            if self.stats.alien_hits < self.setting.max_alien_hits:
                self.stats.alien_hits += len(aliens_hit)
            else: 
                self.stats.game_active = False
                break

        # If all aliens are destroyed, create a new fleet
        if not self.aliens:
            self.bullets.empty()

    def _update_target(self):
        """Update positions of all aliens and check for collisions with the ship or left screen edge."""
        self.target.update()

        # Check for collision between any alien and the ship
        # if pygame.sprite.spritecollideany(self.ship, self.target):
        #     self._ship_hit()

        if self.target.check_edges():
            self.setting.target_direction *= -1
    
    def _ship_hit(self):
        """
        Respond to the ship being hit by an alien.

        Decrements ships_left and ship_hits, resets the fleet and bullets, and pauses briefly.
        Ends the game if no ships remain.
        """

        if self.stats.ships_left > 0:
            # Update ship and hit statistics
            self.stats.ships_left -= 1
            self.stats.ship_hits += 1

            # Clear remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False

    def run_game(self):
        """Start the main game loop, handling events, updates, and drawing each frame."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self._update_bullets()
                self.ship.update()
                self._update_target()

            self._update_screen()

            # Limit the game to 60 frames per second
            self.clock.tick(60)

# Create the game instance and start the game
shooter_ship = Game()
shooter_ship.run_game()
