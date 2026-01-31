class Setting:
    """A class to store all settings for the Sideways Shooter game."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 870
        # White background
        self.bg_color = (255, 255, 255)

        # Ship settings
        self.ship_speed = 15
        self.ship_limit = 3

        # target settings
        self.target_speed = 5
        self.target_width = 50
        self.target_height = 75
        self.target_color = (3, 26, 96)
        self.target_direction = 1
        self.missed_bullet_limit = 3

        # Bullet settings
        self.bullet_speed = 10
        self.bullet_width = 15
        self.bullet_height = 1000
        self.bullet_color = (60, 60, 60)

        self.level_up_scale = 1.3

    def level_up(self):
        self.target_speed *= self.level_up_scale