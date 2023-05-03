import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cloud import Cloud
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, CLOUD, SHIELD_TYPE

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.clouds = []
        self.obstacle_counter = 0
        self.cloud_counter = 0

    def generate_obstacle(self):
        obstacle = random.choice([Cactus(random.choice([SMALL_CACTUS, LARGE_CACTUS])), Bird(BIRD)])
        return obstacle
    
    def update(self, game):
        self.obstacle_counter += 1
        self.cloud_counter += 1
        #crear obstaculos en intervalos de tiempo aleatorios
        if self.obstacle_counter > 80:
            self.obstacle_counter = random.randint(20,60)
            obstacle = self.generate_obstacle()
            self.obstacles.append(obstacle)
        #crear nubes en intervalos de tiempo aleatorios
        if self.cloud_counter > 40:
            self.cloud_counter =  random.randint(0,35)
            cloud = self.generate_cloud()
            self.clouds.append(cloud)
        #colision de obstaculos con el player
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type != SHIELD_TYPE:
                    pygame.time.delay(2000)
                    game.death_count += 1
                    game.playing = False
                    break
                else:
                    self.obstacles.remove(obstacle)
        
        for cloud in self.clouds:
            cloud.update(game.game_speed, self.clouds)

    
    def generate_cloud(self): #crear nube en posicion aleatoria
        cloud = Cloud(CLOUD, random.randint(0, 100))
        return cloud
        
    def draw(self, screen):
        #dibujar todas las nubes
        for cloud in self.clouds:
            cloud.draw(screen)
        #dibujar todos los obstaculos
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles = []
        self.obstacle_counter = 0