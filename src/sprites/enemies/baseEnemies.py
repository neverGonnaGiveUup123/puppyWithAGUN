import pygame
from src.sprites.bullet.bullet import Bullet

class Drone:
    def __init__(self, health: int, damage: int, img: pygame.Surface, spawn: tuple, screen: pygame.Surface, target: list) -> None:
        self.health = health
        self.damage = damage
        self.img = img 
        self.spawn = spawn
        self.screen = screen
        self.target = target

    def move_towards(self, target: list, distance: int):
        if abs(self.spawn[0] - target[0]) > distance:
            pass
    
    def attack(self):
        return Bullet(10, 0, pygame.image.load("src/sprites/bullet/BULLET.png"), self.screen, 50, 5, self.spawn, self.target)
    
    def update_self(self):
        self.screen.blit(self.img, self.spawn)
    
    def return_pos(self):
        return self.spawn
    
    
    # def update(self):
    #     self.bullet.handle_bullet()