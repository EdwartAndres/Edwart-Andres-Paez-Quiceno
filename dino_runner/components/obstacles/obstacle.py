from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):
    def __init__(self, image, obstacle_type):
        self.image = image
        self.obstacle_type = obstacle_type
        self.define_type()
        self.rect.x = SCREEN_WIDTH  
        self.counter = 0
    
    def define_type(self):
        if self.obstacle_type == 3: #type 3 = bird
            self.rect = self.image[0].get_rect()
        else: # si no, es cactus
            self.rect = self.image[self.obstacle_type].get_rect()
    
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        #contador para la animacion de las aver
        if self.obstacle_type == 3:
            self.counter = self.counter + 0.1 if self.counter < 1 else 0
        #----------------------------------------------------------------
        if self.rect.x < -self.rect.width:
            obstacles.pop(0) #elimina el primer obstaculo

    def draw(self, screen):
        if self.obstacle_type == 3: #dibuja el ave
            screen.blit(self.image[round(self.counter)], (self.rect.x, self.rect.y))
        else: #dibuja el cactus
            screen.blit(self.image[self.obstacle_type], (self.rect.x, self.rect.y))
