from dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite


class Cloud(Sprite):

    Y_POS = 220

    def __init__(self, image, y_pos):
        self.image = image
        self.image_rect = image.get_rect()
        self.image_rect.x = SCREEN_WIDTH
        self.image_rect.y = self.Y_POS + y_pos

    def update(self, game_speed, clouds):
        #mover nubes hacia atras
        self.image_rect.x -= (game_speed -2)
        #destruir la primera nube
        if self.image_rect.x < -self.image_rect.width:
            clouds.pop(0)
    
    def draw(self, screen):
        screen.blit(self.image, (self.image_rect.x, self.image_rect.y))
