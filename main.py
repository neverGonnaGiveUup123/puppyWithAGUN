import sys
import pygame
from settings import *
from newSprites import Sprites

pygame.init()

pygame.display.set_caption(WINDOWCAPTION)

pygame.display.set_gamma(GAMMA[0],GAMMA[1],GAMMA[2])

clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode(SCREENDIMENSIONS)

Sprites.screen = SCREEN
player = Sprites.Player(16, pygame.image.load(PLAYERSKINDEFAULT))
Sprites.Drone(pygame.image.load('BULLET.png'), [500,500], 4, player.return_player_pos())

while True:
    SCREEN.fill((0,0,0))
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    Sprites.sprite_loop()
    pygame.display.flip()