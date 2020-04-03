import pygame, pathlib
class Tiles(pygame.sprite.Sprite):
    """A class to create the tiles for the game"""

    def __init__(self, screen, x = 0, y = 290):
        pygame.sprite.Sprite.__init__(self)
        """Initialize the attributes of the tile"""
        self.screen = screen
        self.screen_width, self.screen_height = pygame.display.get_surface().get_rect().size

        # Initialize the image and the rect
        tile_path = str(pathlib.Path('images/tile1.png').expanduser().resolve())
        self.image = pygame.image.load(tile_path)
        self.rect = self.image.get_rect().move(x, y)
    












