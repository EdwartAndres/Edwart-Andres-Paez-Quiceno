import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.menu import Menu
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


class Game:
    GAME_SPEED = 20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu('Press any key to start...', self.screen)       
        self.running = False
        self.death_count = 0
        self.score = 0
        self.highest_score = 0
        self.background_color = 0
        self.background_dark = False
        self.background_color_count = 0
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.obstacle_manager.reset_obstacles()
        self.player.reset_dinosaur()
        self.score = 0
        self.background_color = 255
        self.background_dark = False
        self.background_color_count = 0
        self.game_speed = self.GAME_SPEED
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.update_background()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.update_score()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((self.background_color, self.background_color, self.background_color))
        self.draw_background()
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.player.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        self.menu.reset_screen_color(self.screen)
        # mostrar datos de puntaje despues de la primera muerte
        if self.death_count > 0:
            self.highest_score = max(self.score, self.highest_score)
            self.menu.show_status(self.score, self.highest_score, self.death_count, self.screen)
            self.menu.update_message(f'Game over. Press any key to restart.')
        
        self.menu.draw(self.screen)    
            
        self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140))
        self.menu.update(self)
    
    def update_score(self):
        self.score += 1

        if self.score % 100 == 0 and self.game_speed < 500:
            self.game_speed += 2

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 24)
        text = font.render(f'Score: {self.score}', False, (0,0,0), (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def update_background(self):
        self.background_color_count +=1
        if self.background_color_count > 200:
            self.background_color_count = 0
            self.background_dark = False if self.background_dark else True
    
        if self.background_dark:
            self.background_color -= (5 * int(self.background_color > 65))
        else:
            self.background_color += 5 * int(self.background_color < 250)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)

            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 24)
                text = font.render(f'{self.player.type} enabled for {time_to_show} seconds', False, (0,0,0), (255,255,255))
                text_rect = text.get_rect()
                text_rect.bottomleft = (200, 50)
                self.screen.blit(text, text_rect)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
