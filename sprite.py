import pygame

pygame.init()

WIDTH = 1366
HEIGHT = 768

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Sprite1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('Images/Sprites/planet_1.png'))
        self.sprites.append(pygame.image.load('Images/Sprites/planet_2.png'))
        self.sprites.append(pygame.image.load('Images/Sprites/planet_3.png'))
        self.sprites.append(pygame.image.load('Images/Sprites/planet_4.png'))
        

        self.current_sprite = 0 #index
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
    
    def animate(self):
        self.is_animating = True
    
    def update(self, speed):
        if self.is_animating == True:
            self.current_sprite += speed

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
                
        self.image = self.sprites[int(self.current_sprite)]

sprites = pygame.sprite.Group()
sprite1 = Sprite1(500, 200)
sprites.add(sprite1)


