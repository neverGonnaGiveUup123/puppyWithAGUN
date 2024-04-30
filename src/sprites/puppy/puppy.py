import pygame

class Puppy(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, screen: pygame.Surface, speed: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.screen = screen
        self.pos = [500,500]
        self.speed = speed
        self.mask = pygame.mask.Mask(self.image.get_size(),True)
    
    def move_right(self):
        self.pos[0] += self.speed
    
    def move_up(self):
        self.pos[1] -= self.speed
    
    def move_left(self):
        self.pos[0] -= self.speed
    
    def move_down(self):
        self.pos[1] += self.speed
    
    def update(self):
        self.screen.blit(self.image,self.pos)