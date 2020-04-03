import pygame
import pathlib
import random

class Mona(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        painting1_path = str(pathlib.Path('images/monalisastate2.png').expanduser().resolve())
        painting8_path = str(pathlib.Path('images/monalisa.png').expanduser().resolve())
        painting10_path = str(pathlib.Path('images/monalisastate4.png').expanduser().resolve())
        self.image = pygame.image.load(painting1_path)
        self.image1 = pygame.image.load(painting8_path)
        self.image2 = pygame.image.load(painting10_path)
        self.rect = self.image.get_rect().move(100, 100)
        
    def blitme(self):
        """BLIT ME"""
        self.screen.blit(self.image, self.rect)

class Hands(pygame.sprite.Sprite):
    """A class to represent Monalisa's hands"""
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_rect().size
        painting7_path = str(pathlib.Path('images/monalisastate3.png').expanduser().resolve())
        self.image = pygame.image.load(painting7_path)
        self.rect = self.image.get_rect().move(self.screen_width - 600, self.screen_height - 120)
    
    def blitme(self):
        """Blit me"""
        self.screen.blit(self.image, self.rect)

class Vangogh(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        painting2_path = str(pathlib.Path('images/vangoghstate2.png').expanduser().resolve())
        painting6_path = str(pathlib.Path('images/vangoghstate1.png').expanduser().resolve())
        painting11_path = str(pathlib.Path('images/vangoghstate4.png').expanduser().resolve())
        self.image = pygame.image.load(painting2_path)
        self.image1 = pygame.image.load(painting6_path)
        self.image2 = pygame.image.load(painting11_path)
        self.rect = self.image.get_rect().move(300, 10)
            
    def blitme(self):
        """BLIT ME"""
        self.screen.blit(self.image, self.rect)
    
class Vangogh2(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        painting3_path = str(pathlib.Path('images/vangogh2state2.png').expanduser().resolve())
        painting6_path = str(pathlib.Path('images/vangogh2state1.png').expanduser().resolve())
        painting12_path = str(pathlib.Path('images/vangogh2state3.png').expanduser().resolve())
        self.image = pygame.image.load(painting3_path)
        self.image1 = pygame.image.load(painting6_path)
        self.image2 = pygame.image.load(painting12_path)
        self.rect = self.image.get_rect().move(650, 40)
        

    def blitme(self):
        """BLIT ME"""
        self.screen.blit(self.image, self.rect)

class Picasso(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        painting4_path = str(pathlib.Path('images/picassostate2.png').expanduser().resolve())
        painting5_path = str(pathlib.Path('images/picassostate1.png').expanduser().resolve())
        painting13_path = str(pathlib.Path('images/picassostate3.png').expanduser().resolve())
        self.image2 = pygame.image.load(painting13_path)
        self.image1 = pygame.image.load(painting5_path)
        self.image = pygame.image.load(painting4_path)
        self.rect = self.image.get_rect().move(900, 10)
        
    def blitme(self):
        """BLIT ME"""
        self.screen.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_rect().size
        player_path = str(pathlib.Path('images/player2.png').expanduser().resolve())
        self.image = pygame.image.load(player_path)
        self.rect = self.image.get_rect().move(self.screen_width//2, (self.screen_height//4)*3)
    
    def blitme(self):
        """BLIT ME"""
        self.screen.blit(self.image, self.rect)

class Table(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_rect().size
        table_path = str(pathlib.Path('images/table.png').expanduser().resolve())
        self.image = pygame.image.load(table_path)
        self.image = pygame.transform.scale(self.image, ((110, 110)))
        self.rect = self.image.get_rect().move(self.screen_width - 150, self.screen_height - 125)
    
    def blitme(self):
        """Draw table"""
        self.screen.blit(self.image, self.rect)

class Vase1(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_rect().size
        table_path = str(pathlib.Path('images/vase1.png').expanduser().resolve())
        self.image = pygame.image.load(table_path)
        self.image = pygame.transform.scale(self.image, ((75, 75)))
        self.rect = self.image.get_rect().move(self.screen_width - 135, self.screen_height - 185)
    
    def blitme(self):
        """Draw table"""
        self.screen.blit(self.image, self.rect)

class Furniture1(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_rect().size
        table_path = str(pathlib.Path('images/furniture1.png').expanduser().resolve())
        self.image = pygame.image.load(table_path)
        self.image = pygame.transform.scale(self.image, ((100, 100)))
        self.rect = self.image.get_rect().move(self.screen_width - 665, self.screen_height - 375)
    
    def blitme(self):
        """Draw table"""
        self.screen.blit(self.image, self.rect)

class Bench(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_rect().size
        table_path = str(pathlib.Path('images/bench.png').expanduser().resolve())
        self.image = pygame.image.load(table_path)
        self.image = pygame.transform.scale(self.image, ((150, 100)))
        self.rect = self.image.get_rect().move(self.screen_width - 665, self.screen_height - 125)
    
    def blitme(self):
        """Draw table"""
        self.screen.blit(self.image, self.rect)

class Stool(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_rect().size
        table_path = str(pathlib.Path('images/stool.png').expanduser().resolve())
        self.image = pygame.image.load(table_path)
        self.image = pygame.transform.scale(self.image, ((100, 100)))
        self.rect = self.image.get_rect().move(self.screen_width - 1150, self.screen_height - 150)
    
    def blitme(self):
        """Draw table"""
        self.screen.blit(self.image, self.rect)

class Ghost(pygame.sprite.Sprite):
    def __init__(self, screen, bm_settings):
        pygame.sprite.Sprite.__init__(self)
        # Screen settings
        self.screen = screen
        self.bm_settings = bm_settings
        self.screen_width, self.screen_height = self.screen.get_rect().size

        # Get rects
        ghost_path = str(pathlib.Path('images/ghost.png').expanduser().resolve())
        ghost_path1 = str(pathlib.Path('images/ghost2.png').expanduser().resolve())
        self.image = pygame.image.load(ghost_path)
        self.image1 = pygame.image.load(ghost_path1)
        self.image = pygame.transform.scale(self.image, ((50, 50)))
        self.image1 = pygame.transform.scale(self.image1, ((50, 50)))
        self.rect = self.image.get_rect().move(self.screen_width - 600, self.screen_height - 200)

    def movement(self):
        """Movement of the ghost"""
        if self.rect.right < self.screen_width and self.bm_settings.ghost_movespeed > 0:
            self.rect.right += self.bm_settings.ghost_movespeed
        elif self.rect.right >= self.screen_width and self.bm_settings.ghost_movespeed > 0:
            self.rect.right = self.screen_width
            self.bm_settings.ghost_movespeed *= -1
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.rect.left > 0 and self.bm_settings.ghost_movespeed < 0:
            self.rect.left += self.bm_settings.ghost_movespeed
        elif self.rect.left <= 0 and self.bm_settings.ghost_movespeed < 0:
            self.rect.left = 0
            self.bm_settings.ghost_movespeed *= -1
            self.image = pygame.transform.flip(self.image, True, False)
        
    def blitme(self):
        """Draw table"""
        self.screen.blit(self.image, self.rect)

