class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (20, 24, 82)

        # Ship settings
        self.ship_limit = 2 #game freezes when 3rd time we r hit

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 220, 20, 60
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 5 #halfed

        # How quickly the game speeds up
        self.speedup_scale = 1.25 #15%more
        # How quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2 
        self.alien_speed_factor = 0.5 #halfed
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
