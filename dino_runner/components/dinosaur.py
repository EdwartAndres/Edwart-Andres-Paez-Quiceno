import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING, DEFAULT_TYPE, SHIELD_TYPE, RUNNING_SHIELD, JUMPING_SHIELD, DUCKING_SHIELD

RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}


class Dinosaur(Sprite):

    X_POS = 150
    Y_POS = 300

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect_x = self.X_POS
        self.dino_rect_y = self.Y_POS
        self.time_animation = 0
        self.jump_speed = -10
        self.in_jump = False
        self.has_power_up = False
        self.power_time_up = 0
    
    def update(self, user_input):
        self.time_animation = self.time_animation + 1 if self.time_animation < 10 else 0

        if self.in_jump:
            if user_input[pygame.K_DOWN]:
                self.jump_speed += 2
            self.jump()
        else:
            self.dino_rect_y = self.Y_POS + (user_input[pygame.K_DOWN] * 40)
            #print(self.jump_speed)
            if user_input[pygame.K_DOWN]:
                self.duck()
            elif user_input[pygame.K_UP]:
                self.in_jump = True
            else:
                self.run()

    def run(self):
        self.image = RUN_IMG[self.type][self.time_animation < 5] 

    def duck(self):
        self.image = DUCK_IMG[self.type][self.time_animation < 5]    

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.dino_rect_y += self.jump_speed * 3
        self.jump_speed += 1

        if self.dino_rect_y >= self.Y_POS:
            self.dino_rect_y = self.Y_POS
            self.in_jump = False
            self.jump_speed = -10

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect_x, self.dino_rect_y)) 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.y = self.dino_rect_y + 15
        self.dino_rect.x = self.dino_rect_x + 20
        self.dino_rect.w -= 40
        self.dino_rect.h -= 40
        #screen.fill((255, 0, 255), self.dino_rect)
    
    def reset_dinosaur(self):
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect_x = self.X_POS
        self.dino_rect_y = self.Y_POS
        self.time_animation = 0
        self.jump_speed = -10
        self.in_jump = False
