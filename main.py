import sys
import pygame
from settings import *
# from src.sprites.puppy.puppy import Puppy
# from src.sprites.bullet.bullet import Bullet
# from src.sprites.enemies.baseEnemies import Drone
from newSprites import Sprites

pygame.init()

pygame.display.set_caption(WINDOWCAPTION)

pygame.display.set_gamma(GAMMA[0],GAMMA[1],GAMMA[2])

clock = pygame.time.Clock()

# bulletImg = pygame.image.load("src/sprites/bullet/BULLET.png")

SCREEN = pygame.display.set_mode(SCREENDIMENSIONS)

# bullets = []

# def handle_keyboard_input():
#     keys = pygame.key.get_pressed()
#     if any(keys):
#         if keys[pygame.K_d]:
#             puppy.move_right()
#         if keys[pygame.K_s]:
#             puppy.move_down()
#         if keys[pygame.K_a]:
#             puppy.move_left()
#         if keys[pygame.K_w]:
#             puppy.move_up()
#         if keys[pygame.K_SPACE]:
#             bullets.append(Bullet(24,5,pygame.image.load('src/sprites/bullet/BULLET.png'),SCREEN,15,5,puppy.return_pos(),pygame.mouse.get_pos()))

#     puppy.update()
    # print(puppy.return_pos())

# enemies = []
# enemies.append(Drone(4,4,pygame.image.load('src/sprites/bullet/BULLET.png'), (800,800), SCREEN, puppy.return_pos()))
# def handle_sprites():
#     # for i in enemies:
#     # bullets.append(i.attack())
    
#     for i in bullets:
#         if i.return_lifetime() == 0:
#             bullets.remove(i)
#         i.handle_bullet()
# bullets.append(enemies[0].attack())
Sprites.screen = SCREEN
Sprites.Player(8, pygame.image.load(PLAYERSKINDEFAULT))

while True:
    SCREEN.fill((0,0,0))
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    Sprites.sprite_loop()
    # print(1)
    pygame.display.flip()