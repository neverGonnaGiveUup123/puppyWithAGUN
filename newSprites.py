import pygame

class Sprites:
    sprites = pygame.sprite.Group()
    screen = None
    
    class Drone(pygame.sprite.Sprite):
        def __init__(self, skin: pygame.Surface, spawn: list, velocity: int, target) -> None:
            super().__init__()
            self.add(Sprites.sprites)
            self.skin = skin
            self.pos = spawn
            self.velocity = velocity
            self.target = target
            self.mask = pygame.mask.from_surface(self.skin)

        def __repr__(self) -> str:
            return "I am a drone!"
        
        # def move_towards_target(self):
        #     if self.pos[0] == self.target[0] and self.pos[1] == self.target[1]:
        #         return

        #     if self.pos[0] >= self.target[0]:
        #         self.pos[0] -= self.velocity
        #     else:
        #         self.pos[0] += self.velocity
            
        #     if self.pos[1] >= self.target[1]:
        #         self.pos[1] -= self.velocity
        #     else:
        #         self.pos[1] += self.velocity

        def update(self):
            # self.move_towards_target()
            Sprites.screen.blit(self.skin, self.pos)
    
    class Player(pygame.sprite.Sprite):
        def __init__(self, velocity: int, skin: pygame.Surface) -> None:
            super().__init__()
            self.add(Sprites.sprites)
            self.velocity = velocity
            self.skin = skin
            self.pos = [0,0]
            self.cooldown = 20
            self.mask = pygame.mask.from_surface(self.skin)

        def __repr__(self) -> str:
            return "I am the player!"
        
        def return_player_pos(self):
            return self.pos
        
        def update(self):
            # print("E")
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_w]:
                self.pos[1] -= self.velocity
            if self.keys[pygame.K_s]:
                self.pos[1] += self.velocity
            if self.keys[pygame.K_a]:
                self.pos[0] -= self.velocity
            if self.keys[pygame.K_d]:
                self.pos[0] += self.velocity
            if self.keys[pygame.K_SPACE]:
                if self.cooldown <= 0:
                    Sprites.Bullet(self.pos, pygame.mouse.get_pos(), 8, pygame.image.load('BULLET.png'), 60)
                    self.cooldown = 20
            
            Sprites.screen.blit(self.skin, self.pos)
            self.cooldown -= 1

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, startCoord: list, endCoord: tuple, velocity: int, skin: pygame.Surface, lifetime: int):
            super().__init__()
            self.add(Sprites.sprites)
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
            # print(self.startCoord)
            # print(self.absGradient)
        
        def __repr__(self) -> str:
            return str(self.lifetime)
        
        def update(self):
            self.lifetime -= 1

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

            if self.lifetime <= 0:
                self.kill()

    @staticmethod
    def sprite_loop():
        for spr in Sprites.sprites:
            # print(Sprites.sprites)
            # print(spr)
            spr.update()
            print(spr)
        print("-------------")