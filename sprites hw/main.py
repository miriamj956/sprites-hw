import pygame
pygame.init()

pygame.display.set_caption("Sprites in pygame")
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode([screen_width, screen_height])

screen.fill("pink")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ely.png")
        self.rect = self.image.get_rect()

sprites = pygame.sprite.Group()

def gameStart():
    ely = Player()
    sprites.add(ely)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        sprites.draw(screen)
        pygame.display.update()

gameStart()