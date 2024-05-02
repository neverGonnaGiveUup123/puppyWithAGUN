import pygame
from src.settings import *

class Bullet:
    bullets = []
    velocity = 16
    image = pygame.image.load("src/sprites/bullet/BULLET.png")
    def __init__(self, velocity: int, damage: int, image: pygame.Surface, screen: pygame.Surface, lifetime: int, cooldown: int):
        # self.velocity = velocity
        self.damage = damage
        self.image = image
        self.screen = screen
        self.lifetime = lifetime
        self.cooldown = cooldown
        self.tmp = self.cooldown


    def create_bullet(self, startingCoord: list, endCoord: list):
        if self.tmp > 0:
            self.tmp -= 1
            return

        currentPos = startingCoord.copy()
        if (endCoord[0] - startingCoord[0]) == 0:
            gradient = 9999999
        else:
            gradient = (endCoord[1] - startingCoord[1]) / (endCoord[0] - startingCoord[0])
        c = currentPos[1] - gradient * currentPos[0]
        self.bullets.append([currentPos, gradient, c, self.lifetime, self.check_negative(abs(gradient), startingCoord, endCoord)])
        self.tmp = self.cooldown

    @classmethod
    def handle_bullet(cls):
        if cls.bullets:
            for bullet in cls.bullets:
                bullet[3] -= 1
                if bullet[3] == 0:
                    cls.bullets.remove(bullet)

                if abs(bullet[1]) <= 1:
                    if bullet[4]:
                        bullet[0][0] -= cls.velocity
                    else:
                        bullet[0][0] += cls.velocity
                    bullet[0][1] = round(bullet[1] * bullet[0][0] + bullet[2])

                elif abs(bullet[1]) > 1:
                    # print(bullet[4])
                    if bullet[4]:
                        bullet[0][1] -= cls.velocity
                    else:
                        bullet[0][1] += cls.velocity
                    bullet[0][0] = (bullet[0][1] - bullet[2]) // bullet[1]
                SCREEN.blit(cls.image, bullet[0])

    @staticmethod
    def check_negative(gradient: int, pos0: list, pos1: list) -> bool:
        if gradient > 1:
            return True if pos0[1] > pos1[1] else False
        else:
            return True if pos0[0] > pos1[0] else False