import pygame

class Puppy(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, screen: pygame.Surface, speed: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self._image = image
        self._screen = screen
        self._pos = [500,500]
        self._speed = speed
        self._mask = pygame.mask.Mask(self._image.get_size(),True)
    
    def move_right(self):
        self._pos[0] += self._speed
    
    def move_up(self):
        self._pos[1] -= self._speed
    
    def move_left(self):
        self._pos[0] -= self._speed
    
    def move_down(self):
        self._pos[1] += self._speed
    
    def update(self):
        self._screen.blit(self._image,self._pos)
    
    def check_collision(self, other):
        if self._mask.overlap(other,(0,0)):
            print("yay")
    
    def return_pos(self):
        return self._pos