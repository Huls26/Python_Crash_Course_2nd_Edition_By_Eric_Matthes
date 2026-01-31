import pygame
import sys
from time import sleep

from ship import Ship
from bullet import Bullet
from target import Target
from setting import Setting
from game_stats import GameStats
from button import Button

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

        # Sprite groups for bullets and target
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)

        self.play_button = Button(self, "play")
        self.hit_button = Button(self, f"Hit Count 0")

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.stats.game_active:
           self._start_game()

    def _start_game(self):
        # Reset the game statistics.
        self.stats.reset_stats()
        self.stats.game_active = True

        self.bullets.empty()

        # Create a new fleet and center the ship.
        self.ship.center_ship()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

    def _check_events(self):
        """Respond to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._key_down_x_y(event)
            elif event.type == pygame.KEYUP:
                self._key_up_x_y(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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

        if not self.stats.game_active:
            self.play_button.draw_button()

        self.hit_button.draw_button()    

        self.target.draw_target()

        # Make the most recent screen visible
        pygame.display.flip()

    def _hit_count_display(self):
        hit_count = self.stats.target_hits
        self.hit_button._prep_msg(f"Hit Count {hit_count}")

        self.hit_button.rect.centerx = self.screen_rect.centerx
        self.hit_button.rect.centery = (
            self.screen_rect.centery - self.hit_button.height * 2
        )

    def _update_bullets(self):
        """
        Update bullet positions and handle missed shots.

        Removes bullets that leave the screen and ends the game
        when the missed bullet limit is reached.
        """
        self.bullets.update()

        # Check for collisions between bullets and aliens
        self._check_bullet_target_collisions()

        # Remove bullets that move off the right side of the screen
        for bullet in self.bullets.copy():
            if bullet.is_bullet_missed():
                self.bullets.remove(bullet)
                self.stats.bullets_missed_count += 1

            if self.stats.bullets_missed_count >= self.setting.missed_bullet_limit:
                self._handle_game_over()
        
        self._hit_count_display()
    
    def _handle_game_over(self):
        """
        Handle the game-over state.

        Stops gameplay, updates the hit count display,
        and makes the mouse cursor visible.
        """
        self.stats.game_active = False

        pygame.mouse.set_visible(True)

    def _check_bullet_target_collisions(self):
        collision = pygame.sprite.spritecollide(self.target, self.bullets, True) 
        
        if collision:
            self.stats.target_hits += 1

    def _update_target(self):
        """Update positions of all aliens and check for collisions with the ship or left screen edge."""
        self.target.update()

        # Check when the target is reaching the top or bottom
        if self.target.check_edges():
            self.setting.target_direction *= -1
    
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
