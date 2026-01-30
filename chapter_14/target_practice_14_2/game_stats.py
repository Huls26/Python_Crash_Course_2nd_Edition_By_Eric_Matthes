class GameStats:
    """Track statistics for Sideways Shooter game."""

    def __init__(self, ai_game):
        """
        Initialize statistics for the game.

        Args:
            ai_game: An instance of the Game class, used to access settings.
        """
        self.settings = ai_game.setting

        # Start the game in an active state
        self.game_active = False

        # Initialize other statistics that can change during the game
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        # Track the number of target hits and ship hits
        # Number of ships remaining
        self.ships_left = self.settings.ship_limit
        self.target_hits = 0
        self.bullets_missed_count = 0