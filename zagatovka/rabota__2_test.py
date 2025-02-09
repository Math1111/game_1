import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки окна
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))  # Заполняем экран белым цветом

# Размеры квадратов
width = 100
height = 75

# Массив прямоугольников
rects = []
colors = []  # Список цветов для каждого квадрата

# Первый верхний левый квадрат
rects.append(pygame.Rect(0,0,width,height))

rects.append(pygame.Rect(0,0,width,height))
rects[-1].topright=(screen_width, 0)

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].bottomright = (screen_width, screen_height)

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].bottomleft = (0, screen_height)

rects.append(pygame.Rect(0,0,width, height))
rects[-1].center=(screen_width//2, screen_height//2)

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Смена цвета квадратов
    for i in range(len(colors)):
        colors[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Отрисовка квадратов новыми цветами
    for i, rect in enumerate(rects):
        pygame.draw.rect(screen, colors[i], rect)

    # Обновление экрана
    pygame.display.flip()

    # Задержка перед следующим изменением
    pygame.time.delay(random.randint(300, 700))

pygame.quit()