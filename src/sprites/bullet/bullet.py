import pygame

class Bullet:
    def __init__(self, velocity: int, damage: int, image: pygame.Surface, screen: pygame.Surface):
        self.velocity = velocity
        self.damage = damage
        self.image = image
        self.bullets = []
        self.screen = screen

    def create_bullet(self, startingCoord: list):
        currentPos = startingCoord.copy()
        mousePos = pygame.mouse.get_pos()
        # print(mousePos)
        gradient = (mousePos[1] - startingCoord[1]) / (mousePos[0] - startingCoord[0])
        c = currentPos[1] - gradient * currentPos[0]
        self.bullets.append([currentPos, gradient, c])
        # print(self.bullets)

    def handle_bullet(self):
        if self.bullets:
            for bullet in self.bullets:
                if bullet[1] <= 1:
                    bullet[0][0] += self.velocity
                    bullet[0][1] = round(bullet[1] * bullet[0][0] + bullet[2])
                elif bullet[1] > 1:
                    bullet[0][1] += self.velocity
                    bullet[0][0] = bullet[0][1] // bullet[1]
                self.screen.blit(self.image, bullet[0])
        print(self.bullets)
        
            


