import pygame

class Bullet:
    def __init__(self, velocity: int, damage: int, image: pygame.Surface, screen: pygame.Surface):
        self.velocity = velocity
        self.damage = damage
        self.image = image
        self.bullets = []
        self.screen = screen

    def create_bullet(self, startingCoord: tuple):
        currentPos = startingCoord
        mousePos = pygame.mouse.get_pos()
        gradient = (mousePos[1] - startingCoord[1]) // (mousePos[0] - startingCoord[0])
        self.bullets.append([currentPos, gradient])
        print(self.bullets)

    def handle_bullet(self):
        if self.bullets:
            for bullet in self.bullets:
                if abs(bullet[1]) <= 1:
                    bullet[0][0] += self.velocity
                    bullet[0][1] = bullet[1] * bullet[0][0]
                elif abs(bullet[1]) > 1:
                    bullet[0][1] += self.velocity
                    bullet[0][0] = bullet[0][1] // bullet[1]
                self.screen.blit(self.image, bullet[0])
        print(self.bullets)
        
            


