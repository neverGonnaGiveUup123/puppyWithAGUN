import pygame

class Sprites:
    sprites = []
    screen = None
    
    class Drone:
        def __init__(self) -> None:
            Sprites.sprites.append(self)
            self.skin = None

        def __repr__(self) -> str:
            return "I am a drone!"
        
        def update(self):
            pass
    
    class Player:
        def __init__(self, velocity: int, skin: pygame.Surface) -> None:
            Sprites.sprites.append(self)
            self.velocity = velocity
            self.skin = skin
            self.playerPos = [0,0]

        def __repr__(self) -> str:
            return "I am the player!"
        
        def return_player_pos(self):
            return self.playerPos
        
        def update(self):
            # print("E")
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_w]:
                self.playerPos[1] -= self.velocity
            if self.keys[pygame.K_s]:
                self.playerPos[1] += self.velocity
            if self.keys[pygame.K_a]:
                self.playerPos[0] -= self.velocity
            if self.keys[pygame.K_d]:
                self.playerPos[0] += self.velocity
            if self.keys[pygame.K_SPACE]:
                self.bullet = Sprites.Bullet(self.playerPos, pygame.mouse.get_pos(), 8, pygame.image.load('BULLET.png'), 60)
                Sprites.sprites.append(self.bullet)
            
            Sprites.screen.blit(self.skin, self.playerPos)

    class Bullet:
        def __init__(self, startCoord: list, endCoord: tuple, velocity: int, skin: pygame.Surface, lifetime: int):
            self.startCoord = startCoord
            self.currentPos = self.startCoord.copy()
            self.endCoord = endCoord
            self.velocity = velocity
            self.skin = skin
            self.lifetime = lifetime

            if self.endCoord[0] - self.startCoord[0] == 0:
                self.gradient = 999
            else:
                self.gradient = (self.endCoord[1] - self.startCoord[1]) / (self.endCoord[0] - self.startCoord[0])
            self.absGradient = abs(self.gradient)
            self.c = self.startCoord[1] - self.startCoord[0] * self.gradient
            print(self.startCoord)
            print(self.absGradient)
        
        def __repr__(self) -> str:
            return "I am a bullet"
        
        def update(self):
            self.lifetime -= 1
            if self.lifetime <= 0:
                Sprites.sprites.remove(self)
                del self
                return

            if self.absGradient <= 1:
                if self.endCoord[0] > self.startCoord[0]:
                    self.currentPos[0] += self.velocity
                    self.currentPos[1] = self.gradient * self.currentPos[0] + self.c
                else:
                    self.currentPos[0] -= self.velocity
                    self.currentPos[1] = self.gradient * self.currentPos[0] + self.c
            else:
                if self.endCoord[1] > self.startCoord[1]:
                    self.currentPos[1] += self.velocity
                    self.currentPos[0] = (self.currentPos[1] - self.c) / self.gradient
                else:
                    self.currentPos[1] -= self.velocity
                    self.currentPos[0] = (self.currentPos[1] - self.c) / self.gradient

            Sprites.screen.blit(self.skin, self.currentPos)
    
    @staticmethod
    def sprite_loop():
        for spr in Sprites.sprites:
            # print(spr)
            spr.update()