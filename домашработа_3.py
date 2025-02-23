import pygame
pygame.init()
import pygame.mixer

# запускаем pygame
pygame.mixer.init()

# определяем количество кадров в секунду
FPS = 120

# создаем объект класса pygame.time.Clock для контроля FPS
clock = pygame.time.Clock()

# создаем окно игры
screen = pygame.display.set_mode((640, 480))

# создаем объект класса pygame.Rect с координатами и размерами экрана
screen_rect = screen.get_rect()

# определяем цвета
MAIN_BACKGROUND_COLOR = (255, 255, 255)
MISSILE_COLOR = (255, 0, 0)
SHIP_COLOR = (0, 0, 255)
LAUNCHER_COLOR = (0, 0, 0)

# Текущий цвет фона
background_color = MAIN_BACKGROUND_COLOR

# создаем объект класса pygame.Rect с координатами и размерами корабля
ship = pygame.Rect(300, 200, 50, 100)  # изменяем ширину и высоту корабля
ship.right = screen_rect.right
ship.centery = screen_rect.centery

# создаем объект для пусковой установки (черный квадрат)
launcher = pygame.Rect(50, screen_rect.centery - 25, 20, 50)  # Пусковая установка с размерами 20x50

# создаем список для торпед
missiles = []

# определяем скорость торпеды и корабля
ship_speed_y = 1
launcher_speed_y = 0

# флаги состояния объектов
ship_alive = True

# переменная для главного цикла игры
running = True

# запускаем основной цикл игры
while running:
    # обрабатываем события
    for event in pygame.event.get():
        # если пользователь закрыл окно, то выходим из цикла
        if event.type == pygame.QUIT:
            running = False

        # если пользователь нажал на клавишу
        elif event.type == pygame.KEYDOWN:
            # если нажата клавиша пробел, создаем новую торпеду
            if event.key == pygame.K_SPACE:
                missile = pygame.Rect(launcher.right, launcher.centery - 5, 10, 10)  # снаряд появляется из пусковой установки
                missile_speed_x = 3
                missile_speed_y = 0
                missiles.append((missile, missile_speed_x, missile_speed_y))  # добавляем торпеду в список

            # если нажата клавиша w, двигаем пусковую установку вверх
            elif event.key == pygame.K_w:
                launcher_speed_y = -2

            # если нажата клавиша s, двигаем пусковую установку вниз
            elif event.key == pygame.K_s:
                launcher_speed_y = 2

        # если клавиша отпущена, останавливаем движение пусковой установки
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                launcher_speed_y = 0

    # Обработка движения торпед
    for missile, missile_speed_x, missile_speed_y in missiles:
        missile.move_ip(missile_speed_x, missile_speed_y)

        # если торпеда выходит за экран, удаляем её
        if not missile.colliderect(screen_rect):
            missiles.remove((missile, missile_speed_x, missile_speed_y))  # удаляем торпеду

    # Обработка столкновения с кораблем
    for i, (missile, missile_speed_x, missile_speed_y) in enumerate(missiles):
        if ship_alive and missile.colliderect(ship):
            missiles.pop(i)  # Удаляем снаряд при столкновении с кораблем

    # Обработка движения корабля
    if ship_alive:
        ship.move_ip(0, ship_speed_y)

    # если нижняя или верхняя кромка корабля выходит за границы экрана
    if ship.bottom > screen_rect.bottom or ship.top < screen_rect.top:
        ship_speed_y = -ship_speed_y

    # Движение пусковой установки (черного квадрата)
    launcher.move_ip(0, launcher_speed_y)

    # Если пусковая установка выходит за границы экрана, не даем ей выйти
    if launcher.top < screen_rect.top:
        launcher.top = screen_rect.top
    if launcher.bottom > screen_rect.bottom:
        launcher.bottom = screen_rect.bottom

    # Заливаем фон
    screen.fill(background_color)

    # Рисуем корабль, если он жив
    if ship_alive:
        pygame.draw.rect(screen, SHIP_COLOR, ship)

    # Рисуем пусковую установку (черный квадрат)
    pygame.draw.rect(screen, LAUNCHER_COLOR, launcher)

    # Рисуем торпеды
    for missile, _, _ in missiles:
        pygame.draw.rect(screen, MISSILE_COLOR, missile)

    # Обновляем дисплей
    pygame.display.flip()

    # Задержка для контроля FPS
    clock.tick(FPS)

# Выход из Pygame
pygame.quit()
