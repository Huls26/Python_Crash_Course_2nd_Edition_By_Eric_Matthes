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
        
        # Track the number of target hits and ship hits
        self.target_hits = 0
        self.bullets_missed_count = 0

        # Initialize other statistics that can change during the game
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        # Number of ships remaining
        self.ships_left = self.settings.ship_limit