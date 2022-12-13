class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        #General settings
        self.game_name = "Alien Invasion"
        self.mouse_visable = True

        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Ship settings
        self.speed = 1.0
        self.yspeed = 0.7


        #Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.allowed_bullets = 3
        self.triple_shot = False

        #Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        #fleet direction 1 = right, -1 = left
        self.fleet_direction = 1
