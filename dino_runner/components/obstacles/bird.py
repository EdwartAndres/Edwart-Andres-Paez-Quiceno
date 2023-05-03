import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):

    def __init__(self, image):
        self.height_position = random.randint(0, 2)
        super().__init__(image, 3)
        self.rect.y = 320 - (self.height_position * 50)
