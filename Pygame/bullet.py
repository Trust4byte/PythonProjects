import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ships current position"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        #Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midtop = ai_game.ship.rect.midtop

        #Store the bullets positon as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        #Update the decimal positon of the bullet
        self.y -= self.settings.bullet_speed

        #Update rect positon
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)


class TBullet(Sprite):
    """A class to manage triple fired bullets from the ship"""

    def __init__(self, ai_game):
        """Create a triple bullet object at the ships current position"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        #Create a triple bullet rect at (0, 0) and then set correct position
        self.create_bullet(ai_game)

        #Store the bullets position as a decimal variable
        self.store_bullet_pos()

    def create_bullet(self, ai_game):
        #super().__init__()
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect2 = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect3 = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midtop = ai_game.ship.rect.midtop
        self.rect2.midtop = (ai_game.ship.rect.midtop[0] + 20, ai_game.ship.rect.midtop[1])
        self.rect3.midtop = (ai_game.ship.rect.midtop[0] - 20, ai_game.ship.rect.midtop[1])

    def store_bullet_pos(self):
        #super().__init__()
        self.y = float(self.rect.y)
        self.y = float(self.rect2.y)
        self.y = float(self.rect3.y)

    def update(self):
        """Move the bullet up the screen"""
        #Update decimal position
        self.y -= self.settings.bullet_speed

        #Update rect position
        self.rect.y = self.y
        self.rect2.y = self.y
        self.rect3.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect2)
        pygame.draw.rect(self.screen, self.color, self.rect3)

