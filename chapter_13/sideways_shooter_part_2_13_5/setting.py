class Setting:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen set
        self.screen_width = 1200
        self.screen_height = 870
        self.bg_color = (255, 255, 255)

        # ship speed
        self.ship_speed = 15

        # Alien settings
        self.alien_speed = 5
        self.fleet_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Bullet settings
        self.bullet_speed = 10
        self.bullet_width = 15
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)