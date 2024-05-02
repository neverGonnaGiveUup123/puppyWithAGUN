import sys
import pygame
from src.settings import *
from src.sprites.puppy.puppy import Puppy
from src.sprites.bullet.bullet import Bullet
from src.sprites.enemies.baseEnemies import E

pygame.init()

pygame.display.set_caption(WINDOWCAPTION)

pygame.display.set_gamma(GAMMA[0],GAMMA[1],GAMMA[2])

clock = pygame.time.Clock()

puppy = Puppy(pygame.image.load("src/sprites/bullet/BULLET.png"), SCREEN, 8)

bulletImg = pygame.image.load("src/sprites/bullet/BULLET.png")
playerBullet = Bullet(24, 0, bulletImg, SCREEN, 30, 10)

enemy = E(30, 30, pygame.image.load('src/sprites/bullet/BULLET.png'), [800,500], SCREEN, puppy.return_pos())

def handle_keyboard_input():
    keys = pygame.key.get_pressed()
    if any(keys):
        if keys[pygame.K_d]:
            puppy.move_right()
        if keys[pygame.K_s]:
            puppy.move_down()
        if keys[pygame.K_a]:
            puppy.move_left()
        if keys[pygame.K_w]:
            puppy.move_up()
        if keys[pygame.K_SPACE]:
            playerBullet.create_bullet(puppy.return_pos(), pygame.mouse.get_pos())

    puppy.update()
    # print(puppy.return_pos())

while True:
    SCREEN.fill((0,0,0))
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    Bullet.handle_bullet()
    # print(pygame.mouse.get_pos())
    enemy.attack()
    enemy.update_self()

    handle_keyboard_input()
    pygame.display.flip()