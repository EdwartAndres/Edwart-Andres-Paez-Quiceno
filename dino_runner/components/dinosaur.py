import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

class Dinosaur(Sprite):
    X_POS = 30
    Y_POS = 310
    JUMP_SPEED = 8.5

    def __init__(self):
        super().__init__()
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.jump_speed = self.JUMP_SPEED
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.step_index = 0 

    def update(self, user_input):
        if self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        else:
            self.run()

            if user_input[pygame.K_UP]:
                if not self.dino_jump and not self.dino_duck:
                    self.dino_jump = True
                    self.dino_run = False
            elif user_input[pygame.K_DOWN]:
                if not self.dino_jump and not self.dino_duck:
                    self.dino_duck = True
                    self.dino_run = False
            else:
                self.dino_jump = False
                self.dino_duck = False
                self.dino_run = True

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_speed * 4
        self.jump_speed -= 1.2
        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.jump_speed = self.JUMP_SPEED
            self.dino_jump = False
    
    def duck(self):
        self.image = DUCKING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS + 40
        if not pygame.key.get_pressed()[pygame.K_DOWN]:
            self.dino_duck = False
            self.dino_run = True

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
