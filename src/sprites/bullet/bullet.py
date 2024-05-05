import pygame
from src.settings import *

class Bullet:
    def __init__(self, velocity: int, damage: int, image: pygame.Surface, screen: pygame.Surface, lifetime: int, cooldown: int, startCoord: tuple, endCoord: tuple):
        self.velocity = velocity
        self.damage = damage
        self.image = image
        self.screen = screen
        self.lifetime = lifetime
        self.cooldown = cooldown
        self.tmp = self.cooldown
        self.rect = self.image.get_rect()
        self.currentPos = [0,0]
        self.gradient = 0
        self.intercept = 0
        self.negativeDirection = False
        self.endCoord = endCoord
        if (self.endCoord[0] - self.currentPos[0]) == 0:
            self.gradient = 9999999
        else:
            self.gradient = (self.endCoord[1] - self.currentPos[1]) / (self.endCoord[0] - self.currentPos[0])

        self.intercept = self.currentPos[1] - self.gradient * self.currentPos[0]
        self.negativeDirection = self.check_negative(abs(self.gradient), self.currentPos, self.endCoord)

    # def create_bullet(self, startingCoord: list, endCoord: list):
    #     if self.tmp > 0:
    #         self.tmp -= 1
    #         return

    #     self.currentPos = startingCoord.copy()
    #     if (endCoord[0] - startingCoord[0]) == 0:
    #         self.gradient = 9999999
    #     else:
    #         self.gradient = (endCoord[1] - startingCoord[1]) / (endCoord[0] - startingCoord[0])

    #     self.intercept = self.currentPos[1] - self.gradient * self.currentPos[0]
    #     self.negativeDirection = self.check_negative(abs(self.gradient), startingCoord, endCoord)
    #     self.tmp = self.cooldown

    def handle_bullet(self):
        if self.tmp > 0:
            self.tmp -= 1
            return
        
        self.lifetime -= 1

        if abs(self.gradient) <= 1:
            if self.negativeDirection:
                self.currentPos[0] -= self.velocity
            else:
                self.currentPos[0] += self.velocity
            self.currentPos[1] = round(self.gradient * self.currentPos[0] + self.intercept)

        elif abs(self.gradient) > 1:
            if self.negativeDirection:
                self.currentPos[1] -= self.velocity
            else:
                self.currentPos[1] += self.velocity
            self.currentPos[0] = (self.currentPos[1] - self.intercept) // self.gradient
        SCREEN.blit(self.image, self.currentPos)
        self.tmp = self.cooldown

    @staticmethod
    def check_negative(gradient: int, pos0: list, pos1: list) -> bool:
        if gradient > 1:
            return True if pos0[1] > pos1[1] else False
        else:
            return True if pos0[0] > pos1[0] else False
    
    def return_lifetime(self):
        return self.lifetime