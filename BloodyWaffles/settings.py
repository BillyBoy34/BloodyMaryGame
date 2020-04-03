class Settings():
    """A class that holds the settings of the game."""

    def __init__(self):
        """Initializing the attributes for the settings"""
        
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 600
        self.screen_caption = 'Bloody Mary'
        self.bg_color = (0, 51, 102)

        # Player Settings
        self.player_movespeed = 7

        # Ghost Settings
        self.ghost_movespeed = -5

        # Game progress flags
        self.puzzle1_solved = False
        self.puzzle2_solved = False
        self.init_hands = False
        self.game_over_text = False
        # Volumes
        #self.bg_music_vol = 0.5





