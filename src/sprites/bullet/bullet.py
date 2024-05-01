import pygame

class Bullet:
    def __init__(self, velocity: int, damage: int, image: pygame.Surface, screen: pygame.Surface, lifetime: int, cooldown: int):
        self.velocity = velocity
        self.damage = damage
        self.image = image
        self.bullets = []
        self.screen = screen
        self.lifetime = lifetime
        self.cooldown = cooldown
        self.tmp = self.cooldown

    def create_bullet(self, startingCoord: list):
        if self.tmp > 0:
            self.tmp -= 1
            return

        currentPos = startingCoord.copy()
        mousePos = pygame.mouse.get_pos()
        gradient = (mousePos[1] - startingCoord[1]) / (mousePos[0] - startingCoord[0])
        c = currentPos[1] - gradient * currentPos[0]
        self.bullets.append([currentPos, gradient, c, self.lifetime, self.check_negative(abs(gradient), startingCoord, mousePos)])
        self.tmp = self.cooldown

    def handle_bullet(self):
        if self.bullets:
            for bullet in self.bullets:
                bullet[3] -= 1
                if bullet[3] == 0:
                    self.bullets.remove(bullet)

                if abs(bullet[1]) <= 1:
                    if bullet[4]:
                        bullet[0][0] -= self.velocity
                    else:
                        bullet[0][0] += self.velocity
                    bullet[0][1] = round(bullet[1] * bullet[0][0] + bullet[2])

                elif abs(bullet[1]) > 1:
                    print(bullet[4])
                    if bullet[4]:
                        bullet[0][1] -= self.velocity
                    else:
                        bullet[0][1] += self.velocity
                    bullet[0][0] = (bullet[0][1] - bullet[2]) // bullet[1]
                self.screen.blit(self.image, bullet[0])

    @staticmethod
    def check_negative(gradient: int, pos0: list, pos1: list) -> bool:
        if gradient > 1:
            return True if pos0[1] > pos1[1] else False
        else:
            return True if pos0[0] > pos1[0] else False