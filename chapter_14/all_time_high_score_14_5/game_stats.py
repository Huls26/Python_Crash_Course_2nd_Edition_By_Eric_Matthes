class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.setting
        # Start Alien Invasion in an active state.
        self.game_active = False

        self.reset_stats()
        self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def load_high_score(self):
        """Load high score from file."""
        try:
            with open("high_score.txt", "r", encoding='utf-8') as file:
                self.high_score = int(file.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0