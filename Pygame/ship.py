import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #Speed
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Start ship in the center
        #self.rect.center = (600, 400)

    def update(self):
        """Update the ships position based on the movementflag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.speed

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.yspeed

        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.yspeed

        #Update rect
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)