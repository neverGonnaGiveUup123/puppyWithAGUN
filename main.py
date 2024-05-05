import sys
import pygame
from src.settings import *
from src.sprites.puppy.puppy import Puppy
from src.sprites.bullet.bullet import Bullet
from src.sprites.enemies.baseEnemies import Drone

pygame.init()

pygame.display.set_caption(WINDOWCAPTION)

pygame.display.set_gamma(GAMMA[0],GAMMA[1],GAMMA[2])

clock = pygame.time.Clock()

puppy = Puppy(pygame.image.load("src/sprites/bullet/BULLET.png"), SCREEN, 8)

bulletImg = pygame.image.load("src/sprites/bullet/BULLET.png")

bullets = []

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
            bullets.append(Bullet(24,5,pygame.image.load('src/sprites/bullet/BULLET.png'),SCREEN,15,5,puppy.return_pos(),pygame.mouse.get_pos()))

    puppy.update()
    # print(puppy.return_pos())

enemies = []
enemies.append(Drone(4,4,pygame.image.load('src/sprites/bullet/BULLET.png'), (800,800), SCREEN, puppy.return_pos()))
def handle_sprites():
    for i in enemies:
        bullets.append(i.attack())
    
    for i in bullets:
        if i.return_lifetime() == 0:
            bullets.remove(i)
        i.handle_bullet()

while True:
    SCREEN.fill((0,0,0))
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    handle_keyboard_input()
    handle_sprites()
    print(1)
    pygame.display.flip()