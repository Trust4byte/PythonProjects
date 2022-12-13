import sys
import pygame as pg
from settings import Settings
from ship import Ship
from bullet import Bullet, TBullet
from alien import Alien

class AlienInvasion:
    def __init__(self):
        pg.init()
        self.settings = Settings()

        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        pg.display.set_caption(self.settings.game_name)
        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()
        self.aliens = pg.sprite.Group()

        self._create_fleet()

        #Invisible Mouse
        pg.mouse.set_visible(self.settings.mouse_visable)

    def run_game(self):
        """Start the main loop for the game"""

        while True:

            self.check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()


    def _update_screen(self):
        # Redraw the screen during each pass throug the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)


        # Make the most recently drawn screen visible
        pg.display.flip()

    def check_events(self):
        # Watch for keyboard and mouse events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            elif event.type == pg.KEYDOWN:
                self.check_keydown_events(event)

            elif event.type == pg.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        if event.key == pg.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True

        if event.key == pg.K_LEFT:
            # Move the ship to the right
            self.ship.moving_left = True

        if event.key == pg.K_UP:
            # Move the ship up
            self.ship.moving_up = True

        if event.key == pg.K_DOWN:
            # Move the ship down
            self.ship.moving_down = True

        if event.key == pg.K_SPACE:
            # Shoot bullets
            self.fire_bullet()

        if event.key == pg.K_o:
            # Activates Bullet op mode
            if self.settings.triple_shot:
                self.settings.triple_shot = False
            else:
                self.settings.triple_shot = True

        if event.key == pg.K_ESCAPE:
            sys.exit()

    def check_keyup_events(self, event):
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False

        if event.key == pg.K_LEFT:
            self.ship.moving_left = False

        if event.key == pg.K_UP:
            self.ship.moving_up = False

        if event.key == pg.K_DOWN:
            self.ship.moving_down = False

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        #Update bullet position
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        # Check for any bullet that have hit aliens
        # If so, get rid of the bullet and the alien

        collisions = pg.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.fleet_drop_speed += 1

    def _update_aliens(self):
        """
        Check if the fleet is at one edge, then
        Update the positions of all aliens in the fleet
        """
        self.check_fleet_edges()
        self.aliens.update()

    def check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

            if alien.check_bottom():
                self.change_fleet_direction(0)
                break


    def change_fleet_direction(self, drop=1):
        """Drop the entire fleet and change the fleet's direction, if drop = 0 aliens won't drop anymore"""
        if drop == 1:
            for alien in self.aliens.sprites():
                alien.rect.y += self.settings.fleet_drop_speed

            self.settings.fleet_direction *= -1

        if drop == 0:
            self.settings.fleet_drop_speed = 0


    def fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if self.settings.triple_shot:
            if len(self.bullets) < self.settings.allowed_bullets:
                new_tbullet = TBullet(self)
                self.bullets.add(new_tbullet)
        else:
            if len(self.bullets) < self.settings.allowed_bullets:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Create a fleet of aliens"""
        # Make a alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #Create the full fleet of aliens
        for row_number in range(number_rows):
            # Create the first row of aliens
            for alien_number in range(number_aliens_x):
                self.create_alien(alien_number, row_number)

    def create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def update_aliens(self):
        """Updates the positon of all aliens in the fleet"""
        self.aliens.update()



if __name__ == '__main__':
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()