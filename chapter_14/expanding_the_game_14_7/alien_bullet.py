from bullet import Bullet

class AlienBullet(Bullet):
    """A class to manage bullets fired by aliens."""

    def __init__(self, ai_game, alien):
        super().__init__(ai_game)
        self.settings = ai_game.setting

        # Override starting position
        self.rect.midbottom = alien.rect.midbottom
        self.y = float(self.rect.y)
        print(self.rect)

    def update(self):
        """Move the bullet down the screen."""
        self.y += self.settings.alien_bullet_speed
        self.rect.y = self.y
