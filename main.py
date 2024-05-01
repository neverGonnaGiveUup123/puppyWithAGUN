import sys
import pygame
from src.settings import *
from src.sprites.puppy.puppy import Puppy
from src.sprites.bullet.bullet import Bullet

pygame.init()

pygame.display.set_caption(WINDOWCAPTION)

pygame.display.set_gamma(GAMMA[0],GAMMA[1],GAMMA[2])

SCREEN = pygame.display.set_mode(WINDOWDIMENSIONS)

clock = pygame.time.Clock()

puppy = Puppy(pygame.image.load("src/sprites/puppy/e.png"), SCREEN, 8)

bulletImg = pygame.image.load("src/sprites/bullet/BULLET.png")
playerBullet = Bullet(24, 0, bulletImg, SCREEN)

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
            playerBullet.create_bullet(puppy.return_pos())

    puppy.update()

while True:
    SCREEN.fill((0,0,0))
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    playerBullet.handle_bullet()
    handle_keyboard_input()
    pygame.display.flip()