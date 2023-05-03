import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:

    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

    def __init__(self, message, screen):
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect =  self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

    def update(self, game):
        pygame.display.update()
        self.hadle_events_on_menu(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))

    def hadle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            elif event.type == pygame.KEYDOWN:
                game.run()
        
    def show_status(self, score, highest_score, total_deaths, screen):
        # lista de datos a mostrar
        datas = [f"Your Score:  {score}", f"Highest Score:  {highest_score}", f"Total Deaths:  {total_deaths}"]
        for data in datas:
            #proceso de mostrar datos uno por uno
            self.text = self.font.render(data, True, (60, 60, 60))
            self.text_rect = self.text.get_rect()
            self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT +60 +(40*datas.index(data)))
            self.draw(screen)

    def update_message(self, message):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)