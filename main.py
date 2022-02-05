import pygame
from pygame.locals import *
import sys
import random

pygame.init()
vec = pygame.math.Vector2

HEIGHT = 500
WIDTH = 500
FPS = 60

frame_per_sec = pygame.time.Clock()

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')


class player(pygame.sprite.Sprite):
    def __init__(self):
        super(player, self).__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((147, 50, 168))
        self.rect = self.surf.get_rect()
        
        self.oldpos = (0, 0)
        self.pos = vec((250, 250))

    def move(self):

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_a]:
            self.pos.x -= 4
        if pressed_keys[K_d]:
            self.pos.x += 4
        if pressed_keys[K_w]:
            self.pos.y -= 4
        if pressed_keys[K_s]:
            self.pos.y += 4

        if self.pos.x >= WIDTH - 15:
            self.pos.x = WIDTH - 15
        if self.pos.x <= 15:
            self.pos.x = 15
        if self.pos.y >= HEIGHT:
            self.pos.y = HEIGHT
        if self.pos.y <= 25:
            self.pos.y = 25

        self.rect.midbottom = self.pos
        self.col()

    def col(self):

        hit = pygame.sprite.spritecollideany(self, platforms)
        if not hit:
            self.oldpos = (self.pos.x, self.pos.y)
        else:
            self.pos.x = self.oldpos[0]
            self.pos.y = self.oldpos[1]
        #print(hit)


class platform(pygame.sprite.Sprite):
    def __init__(self):
        super(platform, self).__init__()
        self.surf = pygame.Surface((random.randint(50, 100), 12))
        self.surf.fill((128, 128, 128))
        self.rect = self.surf.get_rect(center=(random.randint(0, WIDTH - 10), random.randint(0, HEIGHT - 30)))


Bot_Border = platform()
Bot_Border.surf = pygame.Surface((WIDTH, 20))
Bot_Border.surf.fill((255, 0, 0))
Bot_Border.rect = Bot_Border.surf.get_rect(center=(250, 500))

Top_Border = platform()
Top_Border.surf = pygame.Surface((WIDTH, 20))
Top_Border.surf.fill((255, 0, 0))
Top_Border.rect = Top_Border.surf.get_rect(center=(250, 0))

Left_Border = platform()
Left_Border.surf = pygame.Surface((20, HEIGHT))
Left_Border.surf.fill((255, 0, 0))
Left_Border.rect = Left_Border.surf.get_rect(center=(0, 250))

Right_Border = platform()
Right_Border.surf = pygame.Surface((20, HEIGHT))
Right_Border.surf.fill((255, 0, 0))
Right_Border.rect = Right_Border.surf.get_rect(center=(500, 250))

platforms = pygame.sprite.Group()
platforms.add(Bot_Border, Top_Border, Left_Border, Right_Border)

Left_Top_One = platform()
Left_Top_One.surf = pygame.Surface((100, 25))
Left_Top_One.surf.fill((255, 0, 0))
Left_Top_One.rect = Left_Top_One.surf.get_rect(left=50, top=50)

Left_Top_Two = platform()
Left_Top_Two.surf = pygame.Surface((30, 60))
Left_Top_Two.surf.fill((255, 0, 0))
Left_Top_Two.rect = Left_Top_Two.surf.get_rect(left=50, top=115)

Left_Top_Three = platform()
Left_Top_Three.surf = pygame.Surface((30, 60))
Left_Top_Three.surf.fill((255, 0, 0))
Left_Top_Three.rect = Left_Top_Three.surf.get_rect(left=120, top=115)

platforms.add(Left_Top_One, Left_Top_Two, Left_Top_Three)

P1 = player()

all_sprites = pygame.sprite.Group()
all_sprites.add(Bot_Border, Top_Border, Left_Border, Right_Border)
all_sprites.add(Left_Top_One, Left_Top_Two, Left_Top_Three)
all_sprites.add(P1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill((0, 0, 0))

    for entity in all_sprites:
        display_surface.blit(entity.surf, entity.rect)

    pygame.display.update()
    frame_per_sec.tick(FPS)
    P1.move()
