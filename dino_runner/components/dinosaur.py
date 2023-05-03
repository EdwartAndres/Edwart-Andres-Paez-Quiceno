import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING

class Dinosaur(Sprite):

    X_POS = 150
    Y_POS = 300

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect_x = self.X_POS
        self.dino_rect_y = self.Y_POS
        self.time_animation = 0
        self.jump_speed = -10
        self.in_jump = False
    
    def update(self, user_input):
        self.time_animation = self.time_animation + 1 if self.time_animation < 10 else 0

        if self.in_jump:
            self.jump()
        else:
            self.dino_rect_y = self.Y_POS + (user_input[pygame.K_DOWN] * 40)

            if user_input[pygame.K_DOWN]:
                self.duck()
            elif user_input[pygame.K_UP]:
                self.in_jump = True
            else:
                self.run()

    def run(self):
        self.image = RUNNING[0] if self.time_animation < 5 else RUNNING[1]   

    def duck(self):
        self.image = DUCKING[0] if self.time_animation < 5 else DUCKING[1]     

    def jump(self):
        self.image = JUMPING
        self.dino_rect_y += self.jump_speed * 3
        self.jump_speed += 1

        if self.dino_rect_y > self.Y_POS:
            self.dino_rect_y = self.Y_POS
            self.jump_speed = -10
            self.in_jump = False

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect_x, self.dino_rect_y)) 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.y = self.dino_rect_y + 15
        self.dino_rect.x = self.dino_rect_x + 20
        self.dino_rect.w -= 40
        self.dino_rect.h -= 30
        #screen.fill((255, 0, 255), self.dino_rect)
