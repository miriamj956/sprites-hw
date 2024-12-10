import pygame
import random
pygame.init()

pygame.display.set_caption("Sprites in pygame")
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])

screen.fill("pink")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ely.png")
        self.image = pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if(pressed_keys[pygame.K_w]):
            self.rect.move_ip(0,-1)
        if (pressed_keys[pygame.K_s]):
            self.rect.move_ip(0,1)
        if (pressed_keys[pygame.K_a]):
            self.rect.move_ip(-1,0)
        if (pressed_keys[pygame.K_d]):
            self.rect.move_ip(1,0)

        if self.rect.left < 0:
            self.rect.left = 0 
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

sprites = pygame.sprite.Group()

def gameStart():
    ely = Player()
    sprites.add(ely)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        pressed_keys = pygame.key.get_pressed()
        ely.update(pressed_keys)
        screen.fill("pink")
        sprites.draw(screen)
        pygame.display.update()

gameStart()
