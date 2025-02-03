import pygame
pygame.init()

size=(1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")

# Задаем цвета
BACKGROUND=(255, 255, 255)

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


