import pygame

class Bullet:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.ship = ai_game.ship

        # Create the bullet rect
        self.bullet_rect = pygame.Rect(
            0, 0, 
            ai_game.setting.bullet_width,
            ai_game.setting.bullet_height)

        self.bullet_rect.midbottom = self.ship.rect.midtop
        
        self.y = float(self.bullet_rect.y)
        self.shoot_bullet = False

    def update(self):
        if self.shoot_bullet:
            self.y -= self.setting.bullet_speed
         
            self.bullet_rect.x = self.ship.rect.midtop[0]
            self.bullet_rect.y = self.y

            pygame.draw.rect(
                self.screen,
                self.setting.bullet_color,
                self.bullet_rect
            )    

        if not self.shoot_bullet:
            self.y = self.ship.rect.midtop[1]


            
        