import pygame
from pygame.sprite import Group
import pathlib
from sprites import Mona, Hands, Vangogh, Vangogh2, Picasso, Player, Table, Vase1, Furniture1, Bench, Stool, Ghost
from settings import Settings
from game_events import GameEvents
from tiles import Tiles
from button import Button

class horrorgame:
    def __init__(self):
        pygame.init()

        # Initialize settings
        self.bm_settings = Settings()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.bm_settings.screen_caption)
        self.screen = pygame.display.set_mode((self.bm_settings.screen_width,
         self.bm_settings.screen_height))

        # Initializing objects
        self.mona = Mona(self.screen)
        self.hands = Hands(self.screen)
        self.vangogh2 = Vangogh2(self.screen)
        self.vangogh = Vangogh(self.screen)
        self.player = Player(self.screen)
        self.picasso = Picasso(self.screen)
        self.table = Table(self.screen)
        self.vase1 = Vase1(self.screen)
        self.furniture1 = Furniture1(self.screen)
        self.stool = Stool(self.screen)
        self.bench = Bench(self.screen)
        self.ghost = Ghost(self.screen, self.bm_settings)
        self.tiles_group = Group()
        self.button = Button(self.bm_settings, self.screen, 'Game Over')
        
        # Initialize Tiles

        # Initialize Game Events
        self.ge = GameEvents(self.screen, self.bm_settings, self.mona, self.vangogh, self.vangogh2, self.picasso, self.player,
        self.tiles_group, self.table, self.vase1, self.furniture1, self.stool, self.bench, self.ghost, self.hands, self.button)
        self.tilemaker()
 
        #self.run = True

        self.rungame()

        
    def rungame(self):
        while True:
            self.ge.eventmanager()
            self.ge.update_screen()
            self.playermovement()
            self.ghost.movement()
            self.clock.tick(60)
            
    def playermovement(self):
        if self.ge.up:
            if self.player.rect.bottom <= self.bm_settings.screen_height//2:
                self.player.rect.bottom == self.bm_settings.screen_height//2
            elif self.player.rect.bottom > self.bm_settings.screen_height//2:
                self.player.rect.y -= self.bm_settings.player_movespeed
        if self.ge.down:
            if self.player.rect.bottom >= self.bm_settings.screen_height:
                self.player.rect.bottom = self.bm_settings.screen_height
            elif self.player.rect.bottom < self.bm_settings.screen_height:
                self.player.rect.y += self.bm_settings.player_movespeed
        if self.ge.right:
            if self.player.rect.right >= self.bm_settings.screen_width:
                self.player.rect.right = self.bm_settings.screen_width
            elif self.player.rect.right < self.bm_settings.screen_width:
                self.player.rect.x += self.bm_settings.player_movespeed
        if self.ge.left:
            if self.player.rect.left <= 0:
                self.player.rect.left = 0
            elif self.player.rect.left > 0:
                self.player.rect.x -= self.bm_settings.player_movespeed

    def tilemaker(self):
        for y in range(290, self.bm_settings.screen_height, 50):
            for x in range(0, self.bm_settings.screen_width, 50):
                self.tiles_group.add(Tiles(self.screen, x, y))


if __name__ == "__main__":
    horrorgame()