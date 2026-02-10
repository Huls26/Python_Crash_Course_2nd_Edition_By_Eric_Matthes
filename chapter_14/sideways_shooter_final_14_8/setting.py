class Setting:
    """A class to store all settings for the Sideways Shooter game."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 870
        # White background
        self.bg_color = (255, 255, 255)

        self.ship_limit = 3

        self.max_alien_hits = 15

        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 15
        self.bullet_speed = 10
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 10