import pygame, sys, random, pathlib, time
pygame.mixer.pre_init(44100, -16, 2, 512)

class GameEvents():
    """Class for all game events"""
    
    def __init__(self, screen, bm_settings, mona, vangogh, vangogh2, picasso, player, tiles_group, table, vase1, furniture1, bench, stool, ghost, 
    hands, button):
        """Initializing the game events attributes"""
        # Screen attributes
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        #self.screen_width, self.screen_height = self.screen.get_rect().size
        # Settings attributes
        self.bm_settings = bm_settings
        # Sprites attributes
        self.mona = mona
        self.hands = hands
        self.vangogh = vangogh
        self.vangogh2 = vangogh2
        self.picasso = picasso
        self.player = player
        self.table = table
        self.vase1 = vase1
        self.furniture1 = furniture1
        self.stool = stool
        self.bench = bench
        self.ghost = ghost
        self.tiles_group = tiles_group
        self.button = button
        self.particles = []
        self.mona_hands = []
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        
        # Background music
        self.background_sound_path = str(pathlib.Path('sounds/background_music.mp3').expanduser().resolve())
        pygame.mixer.music.load(self.background_sound_path)
        pygame.mixer.music.play(-1)
        
       
        
          
    def eventmanager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.puzzle_1(mouse_x, mouse_y)
                self.puzzle_2(mouse_x, mouse_y)

    def particle_vangogh(self):
        """Particle effects for vangogh if puzzle is solved"""
        self.particles.append([[406, 178], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])

        for particle in self.particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 0.2
            pygame.draw.circle(self.screen, (255, 0, 0), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                self.particles.remove(particle)

   
    def puzzle_1(self, mouse_x, mouse_y):
        """This is the first puzzle (could be last) of the game"""
        # picassos2 = picasso state 2 (naming convention given to IMGs)
        ps2_clicked = self.picasso.rect.collidepoint(mouse_x, mouse_y)
        if ps2_clicked:
            self.picasso.image = pygame.transform.scale(self.picasso.image, (350, 450))
            self.picasso.rect = self.picasso.image.get_rect()
            self.state_1 = 610 < mouse_x < 647 and 219 < mouse_y < 261
            self.picasso.rect.center = self.screen_rect.center
            if self.state_1:
                self.picasso.image = self.picasso.image1
                self.picasso.rect = self.picasso.image1.get_rect().move(900, 10)
                self.vangogh.image = self.vangogh.image1
                self.vangogh.rect = self.vangogh.image1.get_rect().move(300, 10)
                self.baby_sounds_path = str(pathlib.Path('sounds/child_scream.wav').expanduser().resolve())
                self.baby_sounds = pygame.mixer.Sound(self.baby_sounds_path)
                self.baby_sounds.play()
                self.bm_settings.puzzle1_solved = True
                
        
    def puzzle_2(self, mouse_x, mouse_y):
        """This is the second puzzle (could be first) of the game"""
        # vangoghscream = vangogh 2 state 2 (naming convention given to IMGs)
        v2scream_clicked = self.vangogh2.rect.collidepoint(mouse_x, mouse_y)
        if v2scream_clicked:
            self.vangogh2.image = pygame.transform.scale(self.vangogh2.image, (350, 450))
            self.vangogh2.rect = self.vangogh2.image.get_rect()
            self.vangogh2.rect.center = self.screen_rect.center
            self.state_2 = 581 < mouse_x < 630 and 284 < mouse_y < 324 
            if self.state_2:
                self.vangogh2.image = self.vangogh2.image1
                self.vangogh2.rect = self.vangogh2.image1.get_rect().move(650, 40)
                self.bm_settings.init_hands = True
                self.hands.rect = self.hands.image.get_rect().move(600, 540)               
                self.mona_hands.append(self.hands.rect)
        self.hands_clicked = 601 < mouse_x < 630 and 547 < mouse_y < 563
        if self.hands_clicked:
            self.mona_hands.pop(0)
            self.mona.image = self.mona.image1
            self.mona.rect = self.mona.image1.get_rect().move(100, 100)
            self.scream_sounds_path = str(pathlib.Path('sounds/scream_1.wav').expanduser().resolve())
            self.scream_sounds = pygame.mixer.Sound(self.scream_sounds_path)
            self.scream_sounds.play()
            self.bm_settings.puzzle2_solved = True
                

    def kill_you_sound(self):
        if self.ghost.rect.colliderect(self.player.rect):
                self.kill_you_path = str(pathlib.Path('sounds/i_will_kill_you.wav').expanduser().resolve())
                self.kill_you = pygame.mixer.Sound(self.kill_you_path)
                self.kill_you.play()

    def game_over(self):
        if self.bm_settings.puzzle1_solved and self.bm_settings.puzzle2_solved:
            self.mona.image = self.mona.image2
            self.picasso.image = self.picasso.image2
            self.vangogh.image = self.vangogh.image2
            self.vangogh2.image = self.vangogh2.image2
            self.ghost.image = self.ghost.image1
            self.bm_settings.game_over_text = True

    def keydown_events(self, event):
        """Holds the keydown events for event manager"""
        if event.key == pygame.K_w:
            self.up = True
            self.kill_you_sound()
        if event.key == pygame.K_s:
            self.down = True
            self.kill_you_sound()
        if event.key == pygame.K_d:
            self.right = True
            self.kill_you_sound()
        if event.key == pygame.K_a:
            self.left = True
            self.kill_you_sound()
       
    def keyup_events(self, event):
        """Holds the keyup events for event manager"""
        if event.key == pygame.K_w:
            self.up = False
        if event.key == pygame.K_s:
            self.down = False
        if event.key == pygame.K_d:
            self.right = False
        if event.key == pygame.K_a:
            self.left = False
    
    def update_sounds(self):
        """Update the sounds of the game"""
        self.sound_effects()

    def update_screen(self):
        """Update the screen"""
        self.screen.fill((0, 51, 102))
        self.tiles_group.draw(self.screen)
        self.furniture1.blitme()
        self.mona.blitme()
        self.vangogh.blitme()
        if self.bm_settings.puzzle1_solved:    
            self.particle_vangogh()
        self.bench.blitme()
        if self.bm_settings.init_hands:
            for hand in self.mona_hands:
                self.hands.blitme()
        self.vangogh2.blitme()
        self.picasso.blitme()
        self.stool.blitme()
        self.player.blitme()
        self.table.blitme()
        self.vase1.blitme()
        self.ghost.blitme()
        self.game_over()
        if self.bm_settings.game_over_text:
            self.button.draw_button()
        pygame.display.flip()