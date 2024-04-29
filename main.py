import sys
import pygame
from src.settings import *
from src.sprites.puppy.puppy import Puppy

pygame.init()

pygame.display.set_caption(WINDOWCAPTION)

pygame.display.set_gamma(GAMMA[0],GAMMA[1],GAMMA[2])

SCREEN = pygame.display.set_mode(WINDOWDIMENSIONS)

clock = pygame.time.Clock()

puppy = Puppy(pygame.image.load("src/sprites/puppy/e.png"), SCREEN, 1)

running = True
while running:
    SCREEN.fill((0,0,0))
    keys = pygame.key.get_pressed()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    if keys[pygame.K_d]:
        puppy.move_right()

    # SCREEN.blit(pygame.image.load("src/sprites/puppy/e.png"), [500,500])
    pygame.display.flip()