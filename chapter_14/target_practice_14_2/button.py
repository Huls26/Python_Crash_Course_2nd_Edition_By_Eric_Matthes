import pygame.font

class Button:
    """A class to create clickable or display-only buttons."""

    def __init__(self, ai_game, msg):
        """Initialize the button's appearance and position."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Button dimensions and visual settings
        self.width, self.height = 200, 50
        self.button_color = (3, 20, 95)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Create the button rect and center it on the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prepare the button message
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Render the text and center it on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                    self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button and its text to the screen."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)