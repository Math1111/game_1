import pygame
pygame.init()

size=(1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")

# Задаем цвета
BACKGROUND=(255, 255, 255)
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
GREEN=(0, 255, 0)
RED=(255, 0, 0)
BLUE=(0, 0, 255)
YELLOW=(255, 255, 0)
GYAN=(0, 255, 255)
MAGENTA=(255, 0, 255)
GRAY=(128, 128, 128)
ORANGE=(255, 165, 0)
PINK=(255, 192, 203)
BROWN=(165, 42, 42)
PURPLE=(128, 0, 128)
LIME=(0, 255, 0)
NAVY=(0, 0, 128)
OLIVE=(128, 128, 0)
MAROON=(128, 0, 0)
TEAL=(0, 128, 128)
SILVER=(192, 192, 192)
GOLD=(255, 215, 0)

FPS=60
clock = pygame.time.Clock()


running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BACKGROUND)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()