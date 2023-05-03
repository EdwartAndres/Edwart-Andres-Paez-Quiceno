from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):
    def __init__(self, image, obstacle_type):
        super().__init__()
        self.image = image[obstacle_type]
        self.obstacle_type = obstacle_type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            obstacles.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def collide_with(self, dinosaur):
        if self.rect.colliderect(dinosaur.dino_rect):
            dinosaur.dino_dead = True

    @staticmethod
    def spawn(image):
        obstacle_types = [0, 1, 2]  # Por ejemplo, tenemos 3 tipos de obstáculos
        obstacle_type = random.choice(obstacle_types)
        obstacle = Obstacle(image, obstacle_type)
        return obstacle
